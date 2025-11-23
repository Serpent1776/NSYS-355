import java.net.*;
import java.awt.Color;
import java.io.*;
import java.util.*;
public class BattleshipClient {
 /* for anyonr who don't the rules of the board game Battleship:
        1. You make your "ships" by pressing buttons in a certain way on the provided GUI
        2. Then, you "attack" by pressing a button on the newly provided GUI
        3. You or the Server's AI wins when the ships of either side are sunk
*/
    public static void main(String[] args) throws Exception {
        int serverPort = 7447;
        DatagramSocket clientSocket = new DatagramSocket();
        Scanner user = new Scanner(System.in);
        System.out.print("Host of server:");
        String host = user.nextLine();
        InetAddress serverAdress = InetAddress.getByName(host);
        String s = "h";
        byte[] sb = s.getBytes();
        DatagramPacket sPacket = new DatagramPacket(sb, sb.length, serverAdress, serverPort);
        clientSocket.send(sPacket);
        byte[] shipData = new byte[2048]; 
        DatagramPacket rec = new DatagramPacket(shipData, shipData.length);
        clientSocket.receive(rec);
        String sentence = new String(rec.getData());
        //System.out.println(sentence); //debug
        String[] thesplit = sentence.split(" ");
        System.out.println("like 2000 by 2000 is x = 4\n");
        System.out.print("Window Size? (500x by 500x): x = ");
        int out = user.nextInt();
        StartingClientGUI buildingBoard = new StartingClientGUI(out, 10, 10, "Battleship Start", thesplit);
        ClientBattleshipGUI hitBoard = new ClientBattleshipGUI(out, 10, 10, "Battleship Attack Board", thesplit);
        buildingBoard.open();
        /* paint test
        boolean sus = true;
        while(sus) {
            System.out.print(buildingBoard.getGameString());
            buildingBoard.paint(new Color(155, 155, 155));
        }*/
       for(int i = 0; i < 4; i++) {
            buildingBoard.resetPoints();
            int range = 0;
            switch(i) {
                case 0: range = 5; buildingBoard.setOverboardText("Make your Carrier! 5 pins!"); break;
                case 1: range = 4; buildingBoard.setOverboardText("Make your Battleship! 4 pins!"); break;
                case 2: range = 3; buildingBoard.setOverboardText("Make your Submarine! 3 pins!"); break;
                case 3: range = 2; buildingBoard.setOverboardText("Make your Patrol Boat! 2 pins!"); break;
            } //makes it so, when a button is pressed, only buttons in at the end of the range are on. 
            //2 means buttons exactly next to it are active 
            //while 5 means buttons that are 4 buttons away from that button are active
            buildingBoard.setRange(range);

           while (buildingBoard.pinsDonTHavePoints()) {
               /*try {
                    System.out.println(buildingBoard.getStart());
                    System.out.println(buildingBoard.getEnd());
                } catch(Exception e) {
                    e.getMessage();
                }*/
               System.out.print(""); //works unless removed because java is tweaking
            }
            String start = buildingBoard.getStart().getActual();
            String end = buildingBoard.getEnd().getActual();
            buildingBoard.addAccepted(new CoordinateString(start), new CoordinateString(end), range);
            buildingBoard.paintall(range);

            String o = /*""*/"from " + start + " to " + end + "\n";
            /*switch(i) {
                case 0: o = "from A1 to E1\n"; break;
                case 1: o = "from A2 to A5\n"; break;
                case 2: o = "from J10 to J8\n"; break;
                case 3: o = "from E4 to D4\n"; break;
            }*/
            byte[] locationData = o.getBytes();
            DatagramPacket locationPacket = new DatagramPacket(locationData, locationData.length, serverAdress, serverPort);
            clientSocket.send(locationPacket);
    }
    buildingBoard.close();
    shipData = new byte[2048];
    rec = new DatagramPacket(shipData, shipData.length);
    clientSocket.receive(rec);
    String clientShips = new String(rec.getData());
    System.out.println(clientShips);
    //System.out.println(clientShips.length()); debugging
    boolean playing = true;
    hitBoard.open();
    while(playing) {
        hitBoard.resetAttack();
        String attack = "";
        while(attack.equals("")) {
            attack = hitBoard.getAttack();
            if(!attack.equals("")) {
                if(new CoordinateString(attack).isInside(hitBoard.getAttackedPoints())) {
                    hitBoard.underboardtext.setText("Shot at point " + attack + " has already been done. Please choose another one!");
                    attack = "";
            } else {
                hitBoard.underboardtext.setText("");
            }
            }
            System.out.print(""); //works unless removed because java is tweaking again
        }
        byte[] attackData = attack.getBytes();
        DatagramPacket attackPacket = new DatagramPacket(attackData, attackData.length, serverAdress, serverPort);
        clientSocket.send(attackPacket);
        hitBoard.addAttacked();
        shipData = new byte[2048];
        rec = new DatagramPacket(shipData, shipData.length);
        clientSocket.receive(rec); //gets if the attack hit and if server had hit one of their ships. 
        String recString = new String(rec.getData()); 
        System.out.println(recString);
        if(recString.contains("You hit us")) {
            hitBoard.paint(new CoordinateString(attack), new Color(255, 120, 120));
        } else {
            hitBoard.paint(new CoordinateString(attack), new Color(190, 190, 190));
        }
        if(recString.contains("won") || recString.contains("lost")) {
            playing = false;
        }
    }
    clientSocket.close();
    hitBoard.close();
    user.close();
    System.exit(0);
    }
    
}