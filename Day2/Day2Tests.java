import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.StringBuilder;
import java.util.ArrayList;

/**
 * @author Paul Armstrong
 * 
 * This class tests the Day2 functions partOne and partTwo
 */

public class Day2Tests {

	public static void main(String[] args) {

		// Run tests on both parts, then run them with the file input
		TestSequence tests = (new Day2Tests()).new TestSequence();
		tests.performTest(Day2.partOne(new int[][] {{5,1,9,5},{7,5,3},{2,4,6,8}}), 18);
		tests.performTest(Day2.partTwo(new int[][] {{5,9,2,8},{9,4,7,3},{3,8,6,5}}), 9);

		tests.printTestResults();
		printInputFileResults();
	}

	// This function will run the solutions with the input file
	private static void printInputFileResults() {
		ArrayList<String> lines = new ArrayList<String>();

		// Read the whole file into an ArrayList
		try {
			Scanner scanner = new Scanner(new File("input.txt"));
			while (scanner.hasNextLine()) {
				lines.add(scanner.nextLine());
			}
			scanner.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		// Transform into a 2D array of ints
		int[][] rows = new int[lines.size()][];
		for (int i = 0; i < lines.size(); i++) {
			String[] numStrings = lines.get(i).replaceAll("\n","").split("\t");
			rows[i] = new int[numStrings.length];
			for (int j = 0; j < numStrings.length; j++) {
				rows[i][j] = Integer.parseInt(numStrings[j]);
			}
		}

		System.out.println("Part one: "+Day2.partOne(rows));
		System.out.println("Part two: "+Day2.partTwo(rows));
	}


	/**
	 * This is a small nested class I created to perform tests without JUnit
	 */
	class TestSequence {
		private int numPassed, numFailed;
		private String test_str;
		
		// Simply set object variables
		public TestSequence() {
			numPassed = 0;
			numFailed = 0;
			test_str = "";
		}
		
		// Prints test info and resets object variables
		public void printTestResults() {
			test_str += "TEST RESULTS - Passed: "+numPassed+", Failed: "+numFailed;
			System.out.println(test_str);

			numPassed = 0;
			numFailed = 0;
			test_str = "";
		}

		// Compare the result with the expected and modify object variables accordingly
		public <T> void performTest(T result, T expected) {
			if (result == expected) {
				numPassed++;
			} else {
				numFailed++;
				test_str += "TEST #"+(numPassed+numFailed)+" FAILED - Expected <"+expected+">, was <"+result+">\n";
			}
		}
	}
}
