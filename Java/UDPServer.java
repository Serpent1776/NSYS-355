import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws Exception {
        int serverPort = 13001;
        DatagramSocket serverSocket = new DatagramSocket(serverPort);
        byte[] recievedData = new byte[2048]; //buffer to hold data
        byte[] recordedData;
        while(true) {
           
            DatagramPacket recievedPacket = new DatagramPacket(recievedData, recievedData.length);
                //packet that stores the buffer
            serverSocket.receive(recievedPacket);
            String sentenceString = new String(recievedPacket.getData());
            System.out.println("Received: " + sentenceString);
            sentenceString = sentenceString.toUpperCase();
            System.out.print("Yelling: " + sentenceString);
            recordedData = sentenceString.getBytes();
            DatagramPacket serverResponse = new DatagramPacket(recordedData, recordedData.length, recievedPacket.getAddress(), recievedPacket.getPort());
            serverSocket.send(serverResponse);


        }
    }
}
