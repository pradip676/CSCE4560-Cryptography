// Pradip Sapkota
// Student ID: 11821781

import java.io.*;
import java.nio.file.*;

public class HW2_QN5 {
    public static void main(String[] args) throws IOException {
        
        // Read plaintext from "plaintext.txt"
        String plaintext = Files.readString(Paths.get("plaintext.txt")).trim();
        System.out.println("Plaintext: " + plaintext);

        // Convert plaintext to hex
        String hexPlaintext = toHex(plaintext);
        System.out.println("Plaintext in Hex: " + hexPlaintext);
        System.out.println();  //leave the blankline 

        // read key from "key.txt"
        String hexKey = Files.readString(Paths.get("key.txt")).trim();
        System.out.println("Key in Hex: " + hexKey);
        System.out.println();  //leave the blankline 

        // Convert key from hex to bytes
        byte[] key = hexToBytes(hexKey);

        // Encryption using XOR with key
        byte[] ciphertext = xor(plaintext.getBytes(), key);
        

        // Convert ciphertext to hex
        String ciphertextinHex = bytesToHex(ciphertext);
        Files.writeString(Paths.get("ciphertext.txt"), ciphertextinHex);
        System.out.println("Ciphertext in Hex: " + ciphertextinHex);
        System.out.println();

        // Decryption 
        byte[] decodedText = xor(ciphertext, key);
        String decodedPlaintext = new String(decodedText);
        Files.writeString(Paths.get("plaintext_dec.txt"), decodedPlaintext);
        
        // print decoded plaintext
        System.out.println("Resulting Plaintext: " + decodedPlaintext);
        System.out.println("Resulting Plaintext in Hex: " + toHex(decodedPlaintext));
  
    }

    // Convert text to hexadecimal
    public static String toHex(String msg) {
        StringBuilder hex = new StringBuilder();
        for (char c : msg.toCharArray()) {
            hex.append(String.format("%02x", (int) c));
        }
        return hex.toString();
    }

    // conversion to byte array
    public static byte[] hexToBytes(String hex) {
        byte[] data = new byte[hex.length() / 2];
        for (int i = 0; i < hex.length(); i += 2) {
            data[i / 2] = (byte) Integer.parseInt(hex.substring(i, i + 2), 16);
        }
        return data;
    }

    // conversion to byte array
    public static String bytesToHex(byte[] bytes) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            hexString.append(String.format("%02x", b));
        }
        return hexString.toString();
    }

    // XOR
    public static byte[] xor(byte[] input, byte[] key) {
        for (int i = 0; i < input.length; i++) 
            input[i] ^= key[i]; 
        return input;
    }
}
