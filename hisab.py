from pygooglechart import PieChart3D
def python_pie3D():
	chart = PieChart3D(250,250)
	chart.add_data([100,200,250,500,900])
	chart.set_pie_labels("Anuj Sid Nikunj Kardam Maru".split())
	print chart.get_url()
	chart.download("hisab.png")
