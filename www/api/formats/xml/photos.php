<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<photos>
<?php foreach ($DATA as $photo) { ?>
  <photo>
    <url><?php echo $photo['url']; ?></url>
    <title><?php echo $photo['title']; ?></title>
    <added><?php echo $photo['added']; ?></added>
    <square><?php echo $photo['square']; ?></square>
    <thumbnail><?php echo $photo['thumbnail']; ?></thumbnail>
    <medium><?php echo $photo['medium']; ?></medium>
    <large><?php echo $photo['large']; ?></large>
  </photo>
<?php } ?>
</photos>
