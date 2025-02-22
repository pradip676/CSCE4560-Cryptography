// Pradip Sapkota
// Student ID: 11821781

import java.io.*;
import java.nio.file.*;

public class HW2QN3 {
    public static void main(String[] args) throws IOException {
        // write plaintext to file
        String message = "Pay $1000 to Bob";
        Files.writeString(Paths.get("plaintext.txt"), message);

        // Read and print plaintext
        String plaintext = Files.readString(Paths.get("plaintext.txt")).trim();
        System.out.println("plaintext.txt file: " + plaintext);

        // Convert text to hex and save to file
        String hexText = toHex(plaintext);
        Files.writeString(Paths.get("plaintext_hex.txt"), hexText);
        System.out.println("plaintext_hex.txt file: " + hexText);

        String convertedText = fromHex(Files.readString(Paths.get("plaintext_hex.txt")).trim());
        System.out.println("Resulting text: " + convertedText);
    }
    //convert text to hex
    public static String toHex(String msg) {
        StringBuilder hex = new StringBuilder();
        for (char c : msg.toCharArray()) 
            hex.append(String.format("%02x", (int) c));
        return hex.toString();
    }
    //comvert hex to text
    public static String fromHex(String hex) {
        StringBuilder text = new StringBuilder();
        for (int i = 0; i < hex.length(); i += 2) 
            text.append((char) Integer.parseInt(hex.substring(i, i + 2), 16));
        return text.toString();
    }
}
