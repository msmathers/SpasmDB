<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<artist>
  <name><?php echo $DATA['name']; ?></name>
  <slug><?php echo $DATA['slug']; ?></slug>
  <country><?php echo $DATA['country']; ?></country>
  <tags>
<?php foreach ($DATA['tags'] as $tag) { ?>  
    <tag>
      <name><?php echo $tag['name']; ?></name>
      <url><?php echo $tag['url']; ?></url>
    </tag>
<?php } ?>
  </tags>
  <similar_artists>
<?php foreach ($DATA['similar'] as $similar) { ?>  
    <similar_artist>
      <name><?php echo $similar['name']; ?></name>
      <url><?php echo $similar['url']; ?></url>
    </similar_artist>
<?php } ?>
  </similar_artists>
  <links>
<?php foreach ($DATA['links'] as $url) { if ($url) { ?>  
    <url><?php echo $url; ?></url>
<?php } } ?>
  <links>
</artist>
