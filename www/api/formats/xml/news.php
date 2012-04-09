<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<news>
<?php foreach ($DATA as $news) { ?>
  <news_item>
    <url><?php echo $news['url']; ?></url>
    <title><![CDATA[<?php echo $news['title']; ?>]]></title>
    <text><![CDATA[<?php echo $news['text']; ?>]]></text>
    <official><?php echo $news['official']; ?></official>
    <added><?php echo $news['added']; ?></added>
  </news_item>
<?php } ?>
</news>
