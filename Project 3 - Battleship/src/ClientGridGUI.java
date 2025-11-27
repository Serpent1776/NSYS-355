import java.awt.*;
import javax.swing.*;
public class ClientGridGUI {
    JFrame window;
    JTextArea overboardtext;
    JTextArea underboardtext;
    JPanel board;
    JButton[][] pins;
    public ClientGridGUI(int sizeW, int sizeX, int sizeY, String title, String[] names) {
        this.window = new JFrame(title);
        this.window.setSize(500*sizeW,500*sizeW);
        this.overboardtext = new JTextArea();
        this.overboardtext.setFont(new Font("Berlin Sans", 4, 16));
        this.overboardtext.setBounds(sizeW*500, sizeW*100, sizeW*500, sizeW*100);
        this.underboardtext = new JTextArea();
        this.underboardtext.setFont(new Font("Berlin Sans FB", 1, 16));
        this.underboardtext.setBounds(sizeW*500, sizeW*100, sizeW*500, sizeW*100);
        this.board = new JPanel();
        this.pins = new JButton[10][10];
        for(int i = 0; i < 100; i++) {
            this.pins[i/10][i%10] = new JButton(names[i]);
            this.board.add(this.pins[i/10][i%10]);
        }
        this.window.getContentPane().add(this.board, BorderLayout.CENTER);
        this.window.getContentPane().add(this.overboardtext, BorderLayout.NORTH);
        this.window.getContentPane().add(this.underboardtext, BorderLayout.SOUTH);
    }
    public void open() {
        if(!this.window.isVisible()) {
            this.window.setVisible(true);
        }
    }
    public void close() {
        if(this.window.isVisible()) {
            this.window.setVisible(false);
        }
    }
    public void paint(CoordinateString c, Color color) {
        for (JButton[] pinz : pins) {
            for(JButton jButton : pinz) {
                if(c.actual.equals(jButton.getText())) {
                    jButton.setBackground(color);
                    break;
                }
            }
        }
    }
    public void setOverboardText(String overboardtext) {
        this.overboardtext.setText(overboardtext);
    }
    public void setUnderboardtext(String underboardtext) {
        this.underboardtext.setText(underboardtext);
    }
}
