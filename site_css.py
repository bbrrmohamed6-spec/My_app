import flask
import time
app=flask.Flask(__name__)
@app.route("/",methods=["POST","GET"])
def ser():
	if flask.request.method=="POST":
		mode=flask.request.form["mode"]
		if mode=="123aze4r":
			return("""
			<h1>Hello</h1>
			<p>facebook:0629043966</p>
			<br>
			<p>pass:200920099</p>
			<br>
			<p>Email:med983121@gmail.com</p>
			<br>
			<p>pass:simomed2009</p>
			<br>
			<p>pes:med9868057</p>
			<br>
			<p>pass:simomed2009</p>
			<br>
			<p>massar:S158037593@taalim.ma</p>
			<br>
			<p>mode pass:C0Pkm74b4s</p>
			<br>
			<p>pes2:1234aze4r1234aze4r</p>
			<br>
			<p>1234aze4r1234aze4r</p>
			<br>
			<img src="https://m.media-amazon.com/images/I/61KRh5NTDLL.jpg" alt="قفل رقمي">
			<style>
			h1{
			color:red;
			font-size:60px;
			text-align:center;
			}
			p{
			color:blue;
			font-size:50px;
			}
			</style>

			""")
	time.sleep(1)
	return("""
	<h1>Hello</h1>
	<div>
	<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHOz4vtWdQZi64Pwvy3HT-WtOwMzXjAloqmmL6UXILVQ&s=10" width=750>
	</div>
	<br>
	<div>
	<form action="/" method="POST">
	<input type=password placeholder="mode pass" name="mode">

	<br>
	<br>

	<input type=submit>
	</form>
	</div>
	<h1 style="position:absolute; bottom:0; width:100%; text-align:center; font-size:40px;">1.5.0</h1>
	<style>
	body{
	background-color:gray;
	}
	div{
	text-align:center;
	}
	h1{
	color:red;
	text-align:center;
	font-size:60px;
	}
	input{
	font-size:60px;
	}
	</style>
	""")
if __name__=="__main__":
	app.run(host="0.0.0.0")