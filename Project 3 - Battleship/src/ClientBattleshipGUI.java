import java.awt.event.*;
import javax.swing.*;

public class ClientBattleshipGUI extends ClientGridGUI {
    String attack; 
    CoordinateString[] attackedPoints; //list of points that were attacked
    int attackedIndex;

    public ClientBattleshipGUI(int sizeW, int sizeX, int sizeY, String title, String[] names) {
        super(sizeW, sizeX, sizeY, title, names);
        this.attack = "";
        this.attackedIndex = 0;
        this.attackedPoints = new CoordinateString[100];
        for(int i = 0; i < 100; i++) {
            this.pins[i/10][i%10].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent attack) {
                    Object button = attack.getSource();
                    if(button instanceof JButton) { //gets attack string from the button that the client pressed.
                       String strattack = ((JButton)button).getText();
                       attackArea(new CoordinateString(strattack));
                    }
                }
            });
        }

    }
    public void attackArea(CoordinateString attackCoord) {
        this.attack = attackCoord.actual;
    }
    public String getAttack() {
        return attack;
    }
    public void resetAttack() {
        attack = "";
    }
    public void addAttacked() {
        this.attackedPoints[this.attackedIndex] = new CoordinateString(this.attack);
        this.attackedIndex++;
    }
    public CoordinateString[] getAttackedPoints() {
        return attackedPoints;
    }
}    


