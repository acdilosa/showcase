<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Adam's Guitar Riffs</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <link rel="stylesheet" href="css/normalize.min.css">
        <link rel="stylesheet" href="css/main.css">

        <script src="js/vendor/modernizr-2.6.2-respond-1.1.0.min.js"></script>
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
        <![endif]-->

        <?php 
            include 'header.php'; 
            $section_name = $_GET['section_name'];
        ?>

        <div class="main-container">
            <div class="main wrapper clearfix">

                <article>
                    <header>
                        <h1>My <?php echo $section_name;?></h1>
                       
                    </header>
                    <section>
                        <h2></h2>
						<ul>
							<?php
							if($handle = opendir('videos/' . $section_name)) {
								while(false !== ($entry = readdir($handle))) {
									$exploded_stuff = explode('.', $entry);
                                    $file_name = implode('.', array_slice($exploded_stuff, 0, -1));
									$ext = end($exploded_stuff);
									if($ext == 'mp4') {
										print "
    										<li><a href='videos/?section=$section_name&file=$entry'>$file_name</a></li>
										";
									}
								}
							}
							?>
						</ul>
                    </section>
                    <section>
                        
                    </section>
                    <footer>
                        
                    </footer>
                </article>

                <aside>
					<img src="/riffs/IMG_0551.JPG"/>
                    <div class="upload-form">
                        <form action="videos/upload_video.php" method="POST" enctype="multipart/form-data">
                            <input type="hidden" name="previous_url" value="<?php echo $_SERVER['HTTP_REFERER']; ?>" />
                            <input type="hidden" name="section_name" value="<?php echo $section_name;?>" />
                            <input type="file" name="video_file" />
                            <input type="submit" value="Upload" />
                        </form>
                    </div>
				</aside>

            </div> <!-- #main -->
        </div> <!-- #main-container -->

        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="js/vendor/jquery-1.9.1.min.js"><\/script>')</script>

        <script src="js/main.js"></script>

        <script>
            var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
    </body>
</html>