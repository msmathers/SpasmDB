<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<artist_query>
<?php foreach ($DATA as $artist) { ?>
  <artist slug="<?php echo $artist['slug']; ?>"><?php echo $artist['name']; ?></artist>
<?php } ?>
</artist_query>
