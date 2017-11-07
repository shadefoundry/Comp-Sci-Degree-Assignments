<!DOCTYPE html>
<!--
Assignment 4 todo list:
-Header that shows current time and date
-Use getdate
-10 store products, 3 shown at random. all must be different
-footer shows hours of operation, street address, telephone number, email address and copyright information
-->
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" title="style" href="style.css"/>
        <title></title>
    </head>

    <body>
    <audio controls autoplay>
    <source src="bgm.mp3" type="audio/mpeg">
    </audio>
        <?php
        date_default_timezone_set('Canada/Eastern');
        ?>
        <div id="header">
            <?php
            $date = getdate(date("U"));
            $day = $date['weekday'];
            $time = $date['hours'];
            $twelveTime = date("h");
            $ampm = date("a");
            echo "$date[weekday], $date[month] $date[mday], $date[year] <br> $twelveTime:$date[minutes] $ampm <br> ";
            if (($day === 'Sunday') || ($time <= 8) && ($time >= 21)) {
                //closed
                echo"Store Closed";
            } else {
                //display the content
                echo "Store Open";}
            ?>
        </div>
        <div id="maincontent">
            <?php
            $date = getdate(date("U"));
            $day = $date['weekday'];
            $time = $date['hours'];
            //if the date is not sunday and its between 8am and 9pm
            if (($day === 'Sunday') || ($time <= 8) && ($time >= 21)) {
                //closed
                echo"<center><h1>Sorry, we're closed! Please come back later!</h1></center>";
            } else {
                //display the content
                $pic = array('img/clown.png', 'img/freddy.png', 'img/jason.png', 'img/leather.png', 'img/michael.png',
                    'img/pinhead.png', 'img/reaper.png', 'img/scream.png', 'img/venom.png', 'img/werewolf.png');
                shuffle($pic);
                echo"<h1>Welcome to Spooky Costumes, the number 1 source for classic horror costumes and accessories!</h1>";
                for ($i = 0; $i < 3; $i++){
                echo "<img src=\"$pic[$i]\" width=\"200\" height=\"300\" class=\"imagepadding\">";}
                echo"<p>Here's 3 of our best daily deals! All of our costumes are hand made and designed to be as accurate to the source material as"
                . "is possible. Our costumes are lovingly crafted by fans of the series that we seek to mimic, and we hope that you will be as"
                        . "satisfied with out work as we are happy to design and create them.</p>";
            }
            ?>

        </div>
        <div id="footer"><!--footer shows hours of operation, street address, telephone number, email address and copyright information-->
            <p>Hours of Operation: 8:00am to 9:00pm<br>
                Location: 781 Main St E, Unit 19. Milton, Ontario<br>
                Phone: (905) 334-3595, Email: SpookyCostumes@hotmail.com, &copy; 2016 Spooky Costumes Inc.
            </p>
        </div>
    </body>
</html>
