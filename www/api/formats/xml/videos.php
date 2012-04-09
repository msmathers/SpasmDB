<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<videos>
<?php foreach ($DATA as $video) { ?>
  <video>
    <url><?php echo $video['url']; ?></url>
    <title><?php echo $video['title']; ?></title>
    <duration><?php echo $video['duration']; ?></duration>
    <thumbnail><?php echo $video['thumbnail']; ?></thumbnail>
    <views><?php echo $video['views']; ?></views>
  </video>
<?php } ?>
</videos>
