import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class StartingClientGUI extends ClientGridGUI {
    CoordinateString start; //start point of a ship
    CoordinateString end; //end point of a ship
    int range; //length of a ship from start to end
    CoordinateString[] alreadyAccepted; //coordinates that are already parts of ships go here
    int alreadyAcceptedIndex; 
   public StartingClientGUI(int sizeW, int sizeX, int sizeY, String title, String[] names) throws ClientStartException {
        super(sizeW, sizeX, sizeY, title, names);
        this.start = null;
        this.end = null;
        this.range = 0;
        this.alreadyAcceptedIndex = 0;
        this.alreadyAccepted = null;
        for(int i = 0; i<100; i++) {
            this.pins[i/10][i%10].addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent buttonPress)  {
                    Object src = buttonPress.getSource();
                    if(src instanceof JButton) { //gets the text of the parent button
                       JButton pin = (JButton)(src);
                       try {
                       int err = setStartAndEnd(pin.getText());
                       if(err == -1) { //rids start status and set things back to normal
                         start = null;
                         setUnderboardtext("");
                       }
                    } catch(ClientStartException e) {
                        setUnderboardtext(e.getMessage());
                    }
                    } 
                }
            });
        }
   }
   //sets the start and end points of a ship
   public int setStartAndEnd(String str) throws ClientStartException {
        if(this.start == null) {
            CoordinateString coStr = new CoordinateString(str);
            boolean coStrAccepted = coStr.isInside(alreadyAccepted);
            if(!coStrAccepted) {
            this.start = new CoordinateString(str);
            return 0;
            } else {throw new ClientStartException("Your ships can't be too next to each other!");}
        }
        if(this.start.getActual().equals(str)) {
            return -1;
        }
        CoordinateString coStr = new CoordinateString(str);
        boolean coStrAccepted = coStr.isInside(alreadyAccepted);
        if(!coStrAccepted && this.start.withinCrossDistance(coStr, range)) {
                this.end = coStr;
                setUnderboardtext("");
                
                return 0; 
        } else {
            if (coStrAccepted) {
                throw new ClientStartException("Your ships can't be too next to each other!");
            } else {
                throw new ClientStartException("that button" + str +  " is not in a " + range + "-pin range of that other button which is " + start.actual);
            }
        }
    }
    public void resetPoints() {
        this.start = null; this.end = null;
    }
    public boolean pinsDonTHavePoints() {
        return (this.start == null) || (this.end == null);
    }
    public void setRange(int range) {
        this.range = range;
    }
    public CoordinateString getStart() {
        return this.start;
    }
    public CoordinateString getEnd() {
        return this.end;
    }
    //adds points of a ship to alreadyAccepted
    public void addAccepted (CoordinateString start, CoordinateString end, int range) {
        String direction = start.direction(end);
                if(alreadyAccepted == null) {
                   alreadyAccepted = new CoordinateString[32];
                }
                    for(int i = 0; i < range; i++) {
                        if(i == 0) {
                            alreadyAccepted[i + alreadyAcceptedIndex] = start;
                        } else if(i == this.alreadyAcceptedIndex + range - 1) {
                            alreadyAccepted[i + alreadyAcceptedIndex] = end;
                        } else if(direction.equals("up")) {
                            alreadyAccepted[i + alreadyAcceptedIndex] = new CoordinateString(start.xSubtract(i - 1) + (start.getY() + 1));
                        } else if(direction.equals("down")) {
                            alreadyAccepted[i + alreadyAcceptedIndex] = new CoordinateString(start.xAdd(i + 1) + (start.getY() + 1));
                        } else if(direction.equals("left")) {
                            alreadyAccepted[i + alreadyAcceptedIndex] = new CoordinateString(start.getX() + (start.ySubtract(i) + 1));
                        } else if(direction.equals("right")) {
                            alreadyAccepted[i + alreadyAcceptedIndex] = new CoordinateString(start.getX() + start.yAdd(i + 1));
                        }
                    }
                    this.alreadyAcceptedIndex += range - 1;
    }
    //paints all points from most recent to least recent
    public void paintall(int range) {
        try {
        for(int i = alreadyAcceptedIndex-range + 1; i <= alreadyAcceptedIndex; i++) {
            paint(this.alreadyAccepted[i], new Color(155, 155, 155));
        }
    } catch (NullPointerException e) {
        
    }
    }
}

