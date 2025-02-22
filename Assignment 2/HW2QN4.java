// Pradip Sapkota
// Student ID: 11821781

import java.io.FileWriter;
import java.security.SecureRandom;

public class HW2QN4 {
    public static void main(String[] args) throws Exception {
        SecureRandom keys = new SecureRandom();
        byte[] key = new byte[16]; 
        keys.nextBytes(key);

        String hexKey = bytesToHex(key);

        FileWriter writer = new FileWriter("key.txt");
        writer.write(hexKey);
        writer.close();

        System.out.println("One-Tim Pad Key:" + hexKey);
    }

    public static String bytesToHex(byte[] bytes) {
        StringBuilder hex = new StringBuilder();
        for (byte b : bytes) {
            hex.append(String.format("%02x", b));
        }
        return hex.toString();
    }
}
