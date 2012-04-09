<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<shows>
<?php foreach ($DATA as $show) { ?>
  <show>
    <url><?php echo $show['url']; ?></url>
    <title><?php echo $show['title']; ?></title>
    <date><?php echo $show['date']; ?></date>
    <location><?php echo $show['location']; ?></location>
    <added><?php echo $show['added']; ?></added>
  </show>
<?php } ?>
</shows>
