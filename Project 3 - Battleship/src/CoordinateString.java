public class CoordinateString {
    String actual;
    String x;
    int y;
    //note only works for actual strings involving things like "A10", "B1", etc.
    public CoordinateString(String actual) {
        this.actual = actual;
        this.x = actual.substring(0,1);
        this.y = Integer.parseInt(actual.substring(1, actual.length())) - 1;
    }
    public int lettertoNum() {
        int xp = 0;
        switch(this.x) {
            case "A": xp = 0; break;
            case "B": xp = 1; break;
            case "C": xp = 2; break;
            case "D": xp = 3; break;
            case "E": xp = 4; break;
            case "F": xp = 5; break;
            case "G": xp = 6; break;
            case "H": xp = 7; break;
            case "I": xp = 8; break;
            case "J": xp = 9; break;
        }   
        return xp;
    }
    //checks if point is within gamerules for ship placement. If you don't know what I mean, use the rules pdf provided.
    public boolean withinCrossDistance(CoordinateString other, int range) {
        int xvalue = Math.abs(this.x.compareTo(other.x));
        boolean xcheck = (xvalue == range-1 || xvalue == 0);
        int yvalue = Math.abs(this.y-other.y);
        boolean ycheck = (yvalue == range-1 || yvalue == 0);
        boolean crossCheck = (xvalue == 0 || yvalue == 0);
        return xcheck && ycheck && crossCheck;
    }
    public void setActual(String actual) {
        this.actual = actual;
        this.x = actual.substring(0,1);
        this.y = Integer.parseInt(actual.substring(1, actual.length())) - 1;
    }
    public String getActual() {
        return actual;
    }
    public String getX() {
        return x;
    }
    public int getY() {
        return y;
    }
    public String xSubtract(int sub) {
        int xp = this.x.compareTo("A");
        if(sub <= xp) {
        xp -= sub;
        }
        switch(xp) {
            default: return "A";
            case 2: return "B";
            case 3: return "C";
            case 4: return "D";
            case 5: return "E";
            case 6: return "F";
            case 7: return "G";
            case 8: return "H";
            case 9: return "I";
            case 10: return "J";
        }   
    }
    public String xAdd(int addant) {
        int xp = this.x.compareTo("A");
        if(addant >= xp) {
        xp += addant;
        }
        switch(xp) {
            case 1: return "A";
            case 2: return "B";
            case 3: return "C";
            case 4: return "D";
            case 5: return "E";
            case 6: return "F";
            case 7: return "G";
            case 8: return "H";
            case 9: return "I";
            default: return "J";
        }
    }
    public int yAdd(int addant) {
        if(y + addant <= 10) {
        return y + addant;
        } else {
            return 10;
        }
    }
    public int ySubtract(int sub) {
        if(y - sub >= 1) {
            return y - sub;
        } else {
            return 1;
        }
    }
    //returns the direction between two coordinate strings. This is further explained below.
    public String direction(CoordinateString other) { 
        String direction = "";
        int xdirection = this.x.compareTo(other.x); //positive means up, negative means down
        int ydirection = this.y - other.y; // positive means to the right, negative means to the left 
        if(xdirection > 0) {
            direction += "up";
        } else if(xdirection < 0) {
            direction += "down";
        }
        if(ydirection > 0) {
                direction += "left";
            } else if(ydirection < 0) {
                direction += "right";
            }
        if(ydirection == 0 && xdirection == 0) {
            direction = "no direction";
        }
        return direction;
    }
    public boolean equals(CoordinateString other) {
        return this.x.equals(other.x) && this.y == other.y;

    }
    //basically, reversed version of string.contains() for Coordinate Strings
    public boolean isInside(CoordinateString[] list) {
        if (list == null) {
            return false;
        }
        try {
        for(CoordinateString coord: list) {
            if(this.equals(coord)) {
                return true;
            }
        }
        return false;
    } catch (NullPointerException e) {
        return false;
    }
    }


}