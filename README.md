<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		<h1>Visual Cryptography</h1>
		<div>
			<h2>Intro</h2>
			<p>The purpose of this project is to visually encrypt an image of a randomly generated password. Visual cryptography is a technique that allows visual images to be encrypted by hiding the information in two or more semi-transparent pictures. The visual encryption employed in this project divides the image into two separate pictures. Decryption is done by overlaying these two images together. This project will produce three images: the two encrypted pictures + the decrypted picture.</p>
			<p>The program is divided into three separate parts:</p>
			<ul>
				<li>createPswd: Generate a random password</li>
				<li>convertToImage: Convert the generated password into an image</li>
				<li>visualCrypt: Encrypt/decrypt the image to produce two shares plus the decrypt image.</li>
			</ul>
			<p>The entire project can be run from the main directory without requiring the user to go to each individual directory. Go to the section <code>To Run</code> to see how to do so.</p>
		</div>
		<div>
			<h2>Getting Started</h2>
			<p>Please make sure the following are installed:</p>
			<ul>
				<li>python3</li>
				<li>PIL (python image)</li>
				<li>imagemagick (bash image)</li>
				<li>gdc compiler for dlang</li>
				<li>make</li>
			</ul>
		</div>
		<div>
			<h2>To Run</h2>
			<p>To run the complete project move into the main directory and type <code>make</code>. The main makefile should do all the necessary compiling, running and file moving. This should produced the following files:</p>
			<ul>
				<li>decryptedPswd.png</li>
				<li>p5wdout1.png</li>
				<li>p5wdout2.png</li>
			</ul>
		</div>
		<div>
			<h2>To clean</h2>
			<p>To clean up the project, move into the main directory and type <code>make clean</code> to clean up the entire project.</p> 
			<p>To clean up individual directories in the project, move into the main directory and type:</p>
			<ul>
				<li><code>make cleanOne</code> to clean up directory createPswd/</li>
				<li><code>make cleanTwo</code> to clean up directory convertToImage</li>
				<li><code>make cleanThree</code> to clean up directory visualCrypt</li>
			</ul>
		</div>
		<div>
			<h2>Notes</h2>
			<ul>
				<li>The program was designed on a UNIX system (Ubuntu).</li>
				<li>Untested on Mac and Windows.</li>
			</ul>
		</div>
		<div>
			<h2>References</h2>
			<ul>
				<li>Visual cryptography (https://en.wikipedia.org/wiki/Visual_cryptography)</li>
				<li>gdc compiler(https://www.howtoinstall.me/ubuntu/18-04/gdc/)</li>
			</ul>
		</div>
	</body>
</html>
