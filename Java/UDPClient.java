import java.net.*;
import java.util.Scanner;
public class UDPClient {
    public static void main(String[] args) throws Exception {
        int serverPort = 13001;
        DatagramSocket clientSocket = new DatagramSocket();
        InetAddress serverAdress = InetAddress.getByName("localhost");
        System.out.print("Give a message please: ");
        Scanner Userinput = new Scanner(System.in);
        String input = Userinput.nextLine();
        byte[] data = input.getBytes();
        DatagramPacket receivedPacket = new DatagramPacket(data, data.length, serverAdress, serverPort);
        clientSocket.send(receivedPacket);
        byte[] recievedData = new byte[2048];
        DatagramPacket recPacket = new DatagramPacket(recievedData, recievedData.length);
        clientSocket.receive(recPacket);
        String sentence = new String(recPacket.getData());
        System.out.println("Recieved:" + sentence);


    }
}