<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<audio>
<?php foreach ($DATA as $audio) { ?>
  <audio_link>
    <title><?php echo $audio['title']; ?></title>
    <url><?php echo $audio['url']; ?></url>
    <added><?php echo $audio['added']; ?></added>
    <?php if ($audio['album']) { ?><album>
      <title><?php echo $audio['album']['title']; ?></title>
      <url><?php echo $audio['album']['url']; ?></url>
    </album><?php } ?>

  </audio_link>
<?php } ?>
</audio>
