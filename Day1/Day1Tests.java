import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.lang.StringBuilder;

/**
 * @author Paul Armstrong
 * 
 * This class tests the Day1 functions partOne and partTwo
 */

public class Day1Tests {

	public static void main(String[] args) {

		// Run tests on both parts, then run them with the file input
		TestSequence tests = (new Day1Tests()).new TestSequence();
		tests.performTest(Day1.partOne(new int[] {1,1,2,2}), 3);
		tests.performTest(Day1.partOne(new int[] {1,1,1,1}), 4);
		tests.performTest(Day1.partOne(new int[] {1,2,3,4}), 0);
		tests.performTest(Day1.partOne(new int[] {9,1,2,1,2,1,2,9}), 9);

		tests.performTest(Day1.partTwo(new int[] {1,2,1,2}), 6);
		tests.performTest(Day1.partTwo(new int[] {1,2,2,1}), 0);
		tests.performTest(Day1.partTwo(new int[] {1,2,3,4,2,5}), 4);
		tests.performTest(Day1.partTwo(new int[] {1,2,3,1,2,3}), 12);
		tests.performTest(Day1.partTwo(new int[] {1,2,1,3,1,4,1,5}), 4);

		tests.printTestResults();
		printInputFileResults();
	}

	// This function will run the solutions with the input file
	private static void printInputFileResults() {
		StringBuilder str = new StringBuilder();

		// Read the file and put it in an ArrayList
		try {
			Scanner scanner = new Scanner(new File("input.txt"));
			while (scanner.hasNext()) {
				str.append(scanner.next());
			}
			scanner.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}

		char[] characters = str.toString().toCharArray();
		int[] numbers = new int[characters.length];
		for (int i = 0; i < characters.length; i++) {
			numbers[i] = characters[i] - 48;
		}
		System.out.println("Output for part one: "+Day1.partOne(numbers));
		System.out.println("Output for part two: "+Day1.partTwo(numbers));
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
			test_str = "==========================\n";
		}
		
		// Prints test info and resets object variables
		public void printTestResults() {
			test_str += "\nTEST RESULTS - Passed: "+numPassed+", Failed: "+numFailed+"\n==========================";
			System.out.println(test_str);

			numPassed = 0;
			numFailed = 0;
			test_str = "==========================\n";
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
