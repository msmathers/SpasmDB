<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<interviews>
<?php foreach ($DATA as $interview) { ?>
  <interview>
    <url><?php echo $interview['url']; ?></url>
    <title><![CDATA[<?php echo $interview['title']; ?>]]></title>
    <text><![CDATA[<?php echo $interview['text']; ?>]]></text>
    <added><?php echo $interview['added']; ?></added>
  </interview>
<?php } ?>
</interviews>
