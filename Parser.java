import java.io.*;

public class Parser {

    public static void main (String[] args) {

	    try{
		    File fileIn  = new File(args[0]);
		    File fileOut = new File("meta_cache.txt");

		    FileReader streamIn = new FileReader(fileIn);
		    FileWriter streamOut = new FileWriter(fileOut);

		    BufferedReader reader = new BufferedReader(streamIn);
		    BufferedWriter writer = new BufferedWriter(streamOut);

		    String line = "";

		    while ((line = reader.readLine()) != null) {
		    	line = line + ", ";
      			writer.write(line);
   			}

   			reader.close();
		    writer.close();
		    streamIn.close();
		    streamOut.close();
	    }
	     

	    catch (FileNotFoundException e){
	       System.err.println("FileCopy: " + e);
	    } 
	    catch (IOException e){
	       System.err.println("FileCopy: " + e);
	    }
	}
}