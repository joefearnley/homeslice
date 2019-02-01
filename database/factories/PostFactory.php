<?php

$factory->define(App\Post::class, function (Faker $faker) {
    return [
        'body' = $faker->realText(300);
    ];
});