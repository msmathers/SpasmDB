<?php echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n"; ?>
<listens>
<?php foreach ($DATA as $stat) { ?>
  <stat date="<?php echo $stat[0]; ?>"><?php echo $stat[1]; ?></stat>
<?php } ?>
</listens>
