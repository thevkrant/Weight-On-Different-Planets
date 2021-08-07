/* Enter your weight in KGs and then choose any number of given planet to find your weight on that planet. */

import java.util.Scanner;

public class WeightsOnPlanets {
    static Scanner keyboard = new Scanner(System.in);

    public static void main(String[] args) {
        double weight = getEarthWeight();
        int choice = getPlanetChoice();
        double realWeight = computeEffectiveWeight(weight, choice);
        System.out.println("Your weight would be " + realWeight + " on that planet. ");
    }

    static double getEarthWeight() {
        System.out.println("Please enter your current Earth weight: ");
        return keyboard.nextDouble();
    }

    static int getPlanetChoice() {

        System.out.println("I have information on the following planets: ");
        System.out.println("1. Mercury");
        System.out.println("2. Venus");
        System.out.println("3. Earth");
        System.out.println("4. Mars");
        System.out.println("5. Jupiter");
        System.out.println("6. Saturn");
        System.out.println("7. Uranus");
        System.out.println("8. Neptune");

        System.out.println("9. Pluto");
        System.out.println("10. Eris");
        System.out.println("11. Ceres");

        System.out.println("12. Moon");
        System.out.println("13. jupiter\'s Titan");
        System.out.println("14. jupiter\'s Europa");

        return keyboard.nextInt();
    }

    static double computeEffectiveWeight(double weight, int choice) {
        double realWeight = 0;

        if (choice == 1)
            realWeight = (weight * 0.377);

        else if (choice == 2)
            realWeight = (weight * 0.904);

        else if (choice == 3)
            realWeight = (weight * 1.0);

        else if (choice == 4)
            realWeight = (weight * 0.379);

        else if (choice == 5)
            realWeight = (weight * 2.527);

        else if (choice == 6)
            realWeight = (weight * 1.064);

        else if (choice == 7)
            realWeight = (weight * 0.904);

        else if (choice == 8)
            realWeight = (weight * 1.136);

        else if (choice == 9)
            realWeight = (weight * 0.063);

        else if (choice == 10)
            realWeight = (weight * 0.083);

        else if (choice == 11)
            realWeight = (weight * 0.0275);

        else if (choice == 12)
            realWeight = (weight * 0.165);

        else if (choice == 13)
            realWeight = (weight * 0.1378);

        else if (choice == 14)
            realWeight = (weight * 0.134);

        return realWeight;
    }
}