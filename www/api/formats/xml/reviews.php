<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<reviews>
<?php foreach ($DATA as $review) { ?>
  <review>
    <url><?php echo $review['url']; ?></url>
    <added><?php echo $review['added']; ?></added>
    <title><![CDATA[<?php echo $review['title']; ?>]]></title>
    <text><![CDATA[<?php echo $review['text']; ?>]]></text>
    <thumbnail><?php echo $review['thumbnail']; ?></thumbnail>
    <?php if ($review['album']) { ?><album>
      <title><?php echo $review['album']['title']; ?></title>
      <url><?php echo $review['album']['url']; ?></url>
    </album><?php } ?>

  </review>
<?php } ?>
</reviews>
