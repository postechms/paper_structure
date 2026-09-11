class Introduction:
	"""Describes the background and purpose of the study."""
	"""여기는 수정된"""
	"""여기는 추가 수정됨"""

	def __init__(self, topic):
		self.topic = topic

	def present(self):
		return f"This study introduces the topic: {self.topic}."

	def newFunction(self):
		pass
		"this is new function"


class LiteratureReview:
	"""Summarizes relevant existing knowledge."""

	def __init__(self, sources=None):
		self.sources = sources or []

	def present(self):
		if not self.sources:
			return "No literature sources have been added."
		return "Relevant sources: " + ", ".join(self.sources) + "."


class Method:
	"""Explains how the study is conducted."""

	def __init__(self, approach):
		self.approach = approach

	def present(self):
		return f"The study uses a {self.approach} approach."


class Results:
	"""Stores and reports the study findings."""

	def __init__(self, findings=None):
		self.findings = findings or []

	def present(self):
		if not self.findings:
			return "No results have been recorded."
		return "Findings: " + "; ".join(self.findings) + "."


class Conclusion:
	"""Summarizes the study and its implications."""

	def __init__(self, summary):
		self.summary = summary

	def present(self):
		return f"Conclusion: {self.summary}"


class Main:
	"""Coordinates all sections of the research document."""

	def __init__(self):
		self.sections = [
			Introduction("object-oriented programming in Python"),
			LiteratureReview(["Python documentation", "OOP design principles"]),
			Method("practical example-based"),
			Results(["The research structure is divided into five sections"]),
			Conclusion("OOP provides a clear and reusable way to organize research content."),
		]

	def run(self):
		for section in self.sections:
			print(section.present())


if __name__ == "__main__":
	Main().run()
