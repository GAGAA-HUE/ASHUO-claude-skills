"""
Research Assistant - 交叉验证与报告生成工具
"""
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
import re


@dataclass
class Source:
    """信息来源"""
    name: str
    url: str
    source_type: str  # government, academic, media, industry, blog, forum
    publish_date: Optional[str] = None

    # 基础权重配置
    AUTHORITY_WEIGHTS = {
        "government": 1.0,
        "academic": 0.9,
        "media": 0.8,
        "industry": 0.7,
        "blog": 0.4,
        "forum": 0.2
    }

    def get_weight(self) -> float:
        return self.AUTHORITY_WEIGHTS.get(self.source_type, 0.3)


@dataclass
class Fact:
    """事实条目"""
    content: str
    sources: List[Source]
    fact_type: str = "news"  # news, data, research

    def get_credibility_score(self) -> float:
        """计算可信度得分"""
        if not self.sources:
            return 0.0

        total_weight = sum(s.get_weight() * self._get_recency_coeff(s) for s in self.sources)
        return min(total_weight / len(self.sources), 1.0)

    def _get_recency_coeff(self, source: Source) -> float:
        """计算时效系数"""
        if not source.publish_date:
            return 0.8  # 默认中等时效

        try:
            pub_date = datetime.fromisoformat(source.publish_date.replace('Z', '+00:00'))
            now = datetime.now()
            days_diff = (now - pub_date).days

            if self.fact_type == "news":
                if days_diff <= 2: return 1.0
                elif days_diff <= 7: return 0.8
                elif days_diff <= 30: return 0.5
                else: return 0.2
            elif self.fact_type == "data":
                if days_diff <= 90: return 1.0
                elif days_diff <= 180: return 0.8
                elif days_diff <= 365: return 0.5
                else: return 0.2
            else:  # research
                if days_diff <= 365*3: return 1.0
                elif days_diff <= 365*5: return 0.8
                else: return 0.5
        except:
            return 0.8

    def get_confirmation_count(self) -> int:
        """获取独立来源确认数量"""
        unique_domains = set()
        for s in self.sources:
            domain = re.sub(r'^https?://', '', s.url).split('/')[0]
            unique_domains.add(domain)
        return len(unique_domains)

    def is_verified(self) -> bool:
        """是否通过多源确认（>=3个独立来源）"""
        return self.get_confirmation_count() >= 3

    def get_credibility_stars(self) -> str:
        """获取星级评级"""
        score = self.get_credibility_score()
        if score >= 0.9: return "⭐⭐⭐⭐⭐"
        elif score >= 0.7: return "⭐⭐⭐⭐"
        elif score >= 0.5: return "⭐⭐⭐"
        elif score >= 0.3: return "⭐⭐"
        else: return "⭐"

    def get_recency_label(self) -> str:
        """获取时效标签"""
        if not self.sources:
            return "🟡 近期"

        newest_coeff = max(self._get_recency_coeff(s) for s in self.sources)
        if newest_coeff == 1.0: return "🟢 最新"
        elif newest_coeff >= 0.8: return "🟡 近期"
        elif newest_coeff >= 0.5: return "🟠 较旧"
        else: return "🔴 过时"


class ContradictionDetector:
    """矛盾检测器"""

    @staticmethod
    def detect_numeric_contradictions(facts: List[Fact]) -> List[Dict]:
        """检测数值型矛盾"""
        contradictions = []

        # 提取包含数字的事实
        numeric_facts = []
        for fact in facts:
            numbers = re.findall(r'\d+(?:\.\d+)?%?', fact.content)
            if numbers:
                numeric_facts.append((fact, numbers))

        # 检查相似表述中的数值差异
        for i, (fact1, nums1) in enumerate(numeric_facts):
            for fact2, nums2 in numeric_facts[i+1:]:
                # 简化：检查是否有相同上下文但不同数值
                if ContradictionDetector._similar_context(fact1.content, fact2.content):
                    for n1, n2 in zip(nums1, nums2):
                        try:
                            v1, v2 = float(n1.rstrip('%')), float(n2.rstrip('%'))
                            if abs(v1 - v2) / max(v1, v2, 1) > 0.1:  # 10%差异阈值
                                contradictions.append({
                                    "topic": fact1.content[:50] + "...",
                                    "value_a": n1,
                                    "source_a": fact1.sources[0].name if fact1.sources else "未知",
                                    "value_b": n2,
                                    "source_b": fact2.sources[0].name if fact2.sources else "未知",
                                    "difference": f"{abs(v1-v2)/max(v1,v2,1)*100:.1f}%"
                                })
                        except:
                            continue

        return contradictions

    @staticmethod
    def _similar_context(text1: str, text2: str) -> bool:
        """判断两段文本是否描述同一事物"""
        # 简化实现：检查关键词重叠度
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        overlap = len(words1 & words2)
        return overlap >= 3 and overlap / max(len(words1), len(words2)) > 0.3


class ReportGenerator:
    """报告生成器"""

    def __init__(self, topic: str):
        self.topic = topic
        self.facts: List[Fact] = []
        self.timestamp = datetime.now().isoformat()

    def add_fact(self, fact: Fact):
        self.facts.append(fact)

    def generate(self) -> str:
        """生成完整报告"""
        verified_facts = [f for f in self.facts if f.is_verified()]
        pending_facts = [f for f in self.facts if not f.is_verified()]

        # 检测矛盾
        contradictions = ContradictionDetector.detect_numeric_contradictions(self.facts)

        # 确定整体验证状态
        if contradictions:
            status = "❌ 存在争议"
        elif pending_facts and not verified_facts:
            status = "⚠️ 部分待验证"
        else:
            status = "✅ 已验证"

        report = f"""# 信息搜集报告：{self.topic}

> 生成时间：{self.timestamp}
> 搜索范围：新闻、官方公告、行业分析、学术来源
> 验证状态：{status}

---

## 核心发现（高可信度）

| 事实 | 可信度 | 来源数 | 时效 |
|------|--------|--------|------|
"""

        # 按可信度排序
        for fact in sorted(verified_facts, key=lambda f: f.get_credibility_score(), reverse=True)[:10]:
            sources_str = ", ".join([s.name for s in fact.sources[:3]])
            report += f"| {fact.content[:60]}{'...' if len(fact.content) > 60 else ''} | {fact.get_credibility_stars()} | {fact.get_confirmation_count()}个来源 | {fact.get_recency_label()} |\n"

        if not verified_facts:
            report += "| 暂无通过多源确认的高可信度信息 | - | - | - |\n"

        # 矛盾部分
        if contradictions:
            report += """
---

## ⚠️ 矛盾与争议

| 议题 | 说法A（来源） | 说法B（来源） | 差异 |
|------|---------------|---------------|------|
"""
            for c in contradictions[:5]:
                report += f"| {c['topic']} | {c['value_a']} ({c['source_a']}) | {c['value_b']} ({c['source_b']}) | {c['difference']} |\n"
            report += "\n> 建议：对存在争议的信息，请结合更多权威来源进行判断\n"

        # 待验证信息
        if pending_facts:
            report += """
---

## 待验证信息

以下信息仅来自少量来源，建议谨慎采信：

"""
            for fact in pending_facts[:5]:
                report += f"- {fact.content[:80]} — 来源：{fact.sources[0].name if fact.sources else '未知'}\n"

        # 来源总览
        all_sources = {}
        for fact in self.facts:
            for source in fact.sources:
                key = source.name
                if key not in all_sources:
                    all_sources[key] = {"source": source, "count": 0}
                all_sources[key]["count"] += 1

        report += """
---

## 信息来源总览

| 来源 | 类型 | 可信度 | 引用次数 |
|------|------|--------|----------|
"""
        for name, data in sorted(all_sources.items(), key=lambda x: x[1]["count"], reverse=True)[:10]:
            s = data["source"]
            stars = "⭐" * int(s.get_weight() * 5)
            report += f"| {name} | {s.source_type} | {stars} | {data['count']} |\n"

        report += """
---

## 使用建议

1. **高可信度信息**（⭐⭐⭐⭐⭐）可放心引用
2. **存在争议的信息**建议进一步核实
3. **待验证信息**仅供参考，不作为决策依据
4. 本报告基于公开可获取信息生成，不保证100%准确性
"""

        return report


def parse_cron_expression(user_input: str) -> Optional[str]:
    """解析用户自然语言时间为cron表达式"""
    user_input = user_input.lower()

    # 每小时
    if "每小时" in user_input or "每小时" in user_input:
        return "7 * * * *"  # 避开整点

    # 每天
    match = re.search(r'每天.*?([0-9]{1,2})[点:：]([0-9]{0,2})', user_input)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        return f"{minute} {hour} * * *"

    # 每周
    weekdays = {"周一": 1, "周二": 2, "周三": 3, "周四": 4, "周五": 5, "周六": 6, "周日": 0, "周末": 0}
    for cn_day, num in weekdays.items():
        if cn_day in user_input:
            match = re.search(r'([0-9]{1,2})[点:：]', user_input)
            hour = int(match.group(1)) if match else 9
            return f"{hour * 10 % 60} {hour} * * {num}"  # 分散分钟避免并发

    # 每月
    if "每月" in user_input:
        match = re.search(r'([0-9]{1,2})[日号]', user_input)
        day = int(match.group(1)) if match else 1
        return f"30 9 {day} * *"

    return None


if __name__ == "__main__":
    # 测试示例
    report = ReportGenerator("AI Agent发展")

    # 添加测试事实
    fact1 = Fact(
        content="OpenAI发布GPT-4 Turbo更新，支持128K上下文",
        sources=[
            Source("OpenAI Blog", "https://openai.com/blog", "industry", "2024-03-15"),
            Source("TechCrunch", "https://techcrunch.com", "industry", "2024-03-15"),
            Source("The Verge", "https://theverge.com", "media", "2024-03-16")
        ]
    )

    report.add_fact(fact1)
    print(report.generate())
