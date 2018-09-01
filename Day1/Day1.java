import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.StringBuilder;

/**
 * @author Paul Armstrong
 * 
 * This class solves the Advent Of Code 2017 Day1 problem's two parts.
 */

public class Day1 {

	/**
	 * Adds the sum of all numbers with a repeat directly after
	 */
	public static int partOne(int[] numbers) {
		int total = 0, length = numbers.length;

		for (int i = 0; i < length; i++) {
			
			// If the number is repeated in the next element, add it to the sum
			if (numbers[i] == numbers[(i + 1) % length]) {
				total += numbers[i];
			}
		}
		return total;
	}

	/**
	 * Adds the sum of all numbers with a repeat half way around the array
	 */
	public static int partTwo(int[] numbers) {
		int total = 0, length = numbers.length;

		for (int i = 0; i < length; i++) {
			
			// If the number is repeated half way around the array, add it to the sum
			if (numbers[i] == numbers[(i + length / 2) % length]) {
				total += numbers[i];
			}
		}
		return total;
	}
}
