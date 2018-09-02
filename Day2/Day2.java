import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.StringBuilder;

/**
 * @author Paul Armstrong
 * 
 * This class solves the Advent Of Code 2017 Day2 problem's two parts.
 */

public class Day2 {

	/**
	 * Finds the checkSum by adding difference between max and min in each row
	 */
	public static int partOne(int[][] rows) {
		int checkSum = 0, max, min;

		for (int[] row : rows) {
			if (row.length > 0) {
				max = row[0];
				min = row[0];

				// Skip the element at 0 because it has been set at the initial max and min
				for (int j = 1; j < row.length; j++) {
					max = (max > row[j]) ? max : row[j];
					min = (min < row[j]) ? min : row[j];
				}
				checkSum += max - min;
			}
		}
		return checkSum;
	}

	/**
	 * Finds the evenDivSum by adding the division of the one divisible combination
	 */
	public static int partTwo(int[][] rows) {
		int evenDivSum = 0;

		// Add up the evenDivSum for each row
		for (int[] row : rows) {
			evenDivSum += getRowEDS(row);
		}

		return evenDivSum;
	}

	/**
	 * Utilized by partTwo to get the evenDivSum of a row
	 */
	private static int getRowEDS(int[] row) {
		
		// Iterate over values to find the pair where one divides the other
		for (int i = 0; i < row.length; i++) {
			for (int j = 0; j < row.length; j++) {
				if (i != j && row[i] % row[j] == 0) {
					return row[i] / row[j];
				}
			}
		}

		// If none is found, return zero
		return 0;
	}
}
