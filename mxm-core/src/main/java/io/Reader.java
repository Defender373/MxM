package io;

import form.Passage;

import java.io.FileNotFoundException;
import java.io.FileReader;

/**
 * Created by celenp on 3/27/2017.
 */
public class Reader {
    public static void read(String filename) {
        try {
            FileReader reader = new FileReader(filename);

            //reader.

            //for(String line : reader.)

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}