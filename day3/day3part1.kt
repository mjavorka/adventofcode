package demo

import kotlin.system.measureTimeMillis

fun main(args : Array<String>) {

    val point: Int = 289326
    part1(point)
}

fun part1(point: Int) {
    var index = 1
    var x = 0
    var y = 0
    var steps = 1
    var left = false
    var right = true
    var up = false
    var down = false
    var direction = 0

    while (index <= point) {

        var forFuckSake = 0
        while (forFuckSake < 2) {

            var step = 1
            while (step <= steps) {
                when {
                    left -> x++
                    right -> x--
                    up -> y++
                    down -> y--
                }

                index++
                step++
                if (index == point) {
                    println("coordinates of $index is [$x][$y]")
                    return
                }

            }

            if (direction < 3) {
                direction++
            } else {
                direction = 0
            }

            when (direction) {
                0 -> { right = true; left = false; up = false; down = false }
                1 -> { up = true; left = false; right = false; down = false }
                2 -> { left = true; up = false; down = false; right = false }
                3 -> { down = true; right = false; up = false; left = false }
            }

            forFuckSake++
        }
        steps++
    }
}
