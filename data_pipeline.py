class StudentScorePipeline:
    def __init__(self, min_score=50):
        if not isinstance(min_score, (int, float)) or isinstance(min_score, bool):
            raise ValueError("min_score must be a valid number")
        self.min_score = min_score

    def clean_records(self, records):
        cleaned = []
        for record in records:
            if not isinstance(record, (tuple, list)) or len(record) != 2:
                continue
            name, score = record
            if not isinstance(name, str) or not name.strip():
                continue
            if not isinstance(score, (int, float)) or isinstance(score, bool):
                continue
            cleaned.append((name.strip().title(), float(score)))
        return cleaned

    def filter_qualified(self, cleaned_records):
        return [
            (name, score)
            for name, score in cleaned_records
            if score >= self.min_score
        ]

    def compute_stats(self, qualified_records):
        if not qualified_records:
            return {"count": 0, "average": 0.0, "top_score": 0.0}

        scores = [score for _, score in qualified_records]
        return {
            "count": len(scores),
            "average": round(sum(scores) / len(scores), 2),
            "top_score": max(scores),
        }

    def format_report(self, qualified_records):
        stats = self.compute_stats(qualified_records)
        lines = [f"{name}: {score}" for name, score in qualified_records]
        lines.append(
            f"Summary -> Qualified: {stats['count']} | Avg: {stats['average']} | Top: {stats['top_score']}"
        )
        return lines

    def run(self, records):
        cleaned = self.clean_records(records)
        qualified = self.filter_qualified(cleaned)
        return self.format_report(qualified)


def sample_students():
    return [
        ("  Daksh ", 88),
        ("", 95),
        ("Diya", 42),
        ("Rohan", "not_a_number"),
        (" Meera ", 76),
        ("Kabir", True),
        ("Ananya", 91),
    ]


if __name__ == "__main__":
    pipeline = StudentScorePipeline(min_score=50)
    for line in pipeline.run(sample_students()):
        print(line)