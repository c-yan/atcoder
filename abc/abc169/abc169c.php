<?php
    fscanf(STDIN, "%d %f", $a, $b);
    echo intdiv($a * intval($b * 100 + 0.5), 100);
?>
