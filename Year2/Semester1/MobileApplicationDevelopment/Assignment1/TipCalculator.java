package com.example.link491.tipcalculator;
/*
*                            __.--|~|--.__                               ,,;/;
                         /~     | |    ;~\                           ,;;;/;;'
                        /|      | |    ;~\\                      ,;;;;/;;;'
                       |/|      \_/   ;;;|\                    ,;;;;/;;;;'
                       |/ \          ;;;/  )                 ,;;;;/;;;;;'
                   ___ | ______     ;_____ |___....__      ,;;;;/;;;;;'
             ___.-~ \\(| \  \.\ \__/ /./ /:|)~   ~   \   ,;;;;/;;;;;'
         /~~~    ~\    |  ~-.     |   .-~: |//  _.-~~--,;;;;/;;;;;'
        (.-~___     \.'|    | /-.__.-\|::::| //~     ,;;;;/;;;;;'
        /      ~~--._ \|   /          `\:: |/      ,;;;;/;;;;;'
     .-|             ~~|   |  /V""""V\ |:  |     ,;;;;/;;;;;' \
    /                   \  |  ~`^~~^'~ |  /    ,;;;;/;;;;;'    ;
   (        \             \|`\._____./'|/    ,;;;;/;;;;;'      '\
  / \        \                             ,;;;;/;;;;;'     /    |
 |            |                          ,;;;;/;;;;;'      |     |
|`-._          |                       ,;;;;/;;;;;'              \
|             /                      ,;;;;/;;;;;'  \              \__________
(             )                 |  ,;;;;/;;;;;'      |        _.--~
 \          \/ \              ,  ;;;;;/;;;;;'       /(     .-~_..--~~~~~~~~~~
 \__         '  `       ,     ,;;;;;/;;;;;'    .   /  \   / /~
 /          \'  |`._______ ,;;;;;;/;;;;;;'    /   :    \/'/'       /|_/|   ``|
| _.-~~~~-._ |   \ __   .,;;;;;;/;;;;;;' ~~~~'   .'    | |       /~ (/\/    ||
/~ _.-~~~-._\    /~/   ;;;;;;;/;;;;;;;'          |    | |       / ~/_-'|-   /|
(/~         \| /' |   ;;;;;;/;;;;;;;;            ;   | |       (.-~;  /-   / |
|            /___ `-,;;;;;/;;;;;;;;'            |   | |      ,/)  /  /-   /  |
 \            \  `-.`---/;;;;;;;;;' |          _'   |T|    /'('  /  /|- _/  //
   \           /~~/ `-. |;;;;;''    ______.--~~ ~\  |u|  ,~)')  /   | \~-==//
     \      /~(   `-\  `-.`-;   /|    ))   __-####\ |a|   (,   /|    |  \
       \  /~.  `-.   `-.( `-.`~~ /##############'~~)| |   '   / |    |   ~\
        \(   \    `-._ /~)_/|  /############'       |X|      /  \     \_\  `\
        ,~`\  `-._  / )#####|/############'   /     |i|  _--~ _/ | .-~~____--'
       ,'\  `-._  ~)~~ `################'           |o| ((~>/~   \ (((' -_
     ,'   `-.___)~~      `#############             |n|           ~-_     ~\_
 _.,'        ,'           `###########              |g|            _-~-__    (
|  `-.     ,'              `#########       \       | |          ((.-~~~-~_--~
`\    `-.;'                  `#####"                | |           "     ((.-~~
  `-._   )               \     |   |        .       |  \                 "
      `~~  _/                  |    \               |   `---------------------
        |/~                `.  |     \        .     |  O    __.---------------
         |                   \ ;      \             |   _.-~
         |                    |        |            |  /  |
          |                   |         |           |/'  |
*~ALL HAIL OUR GLORIOUS RULER, THE WARRIOR KING, LORD ANGUS McFIFE THE THIRTEENTH~*
* */
import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

import java.text.DecimalFormat;
/* Regarding Changes I have made from the basic assignment:
    -We spoke earlier in the week about changing a tip spinner to a seekBar (slider). You said it
    was fine so that is what I have done. This code now works with one slider and one spinner as
    opposed to two spinners.

    -The Add HST checkbox will not clear the tip %, Number of People Spinner or the Entered Price.
        ->This is for the sake of user convenience. Perhaps they want to check the price with and
        without HST, or check the hst split. It would be annoying to clear everything and lose data.

    -This is the same for the User Input field. It will not clear the Checkbox or tip slider since
     it might be aggravating to the user. It will still clear the price displays.
*/

//and right off the bat we've got wierdness with reimplementing seekbar listeners
public class TipCalculator extends AppCompatActivity implements SeekBar.OnSeekBarChangeListener{
    //declare all of our widgets
    Button btn_tip10, btn_tip15, btn_tip20, btn_Calculate, btn_Clear;
    EditText input_initialAmount;
    CheckBox chk_AddHST;
    SeekBar slider_tip;
    TextView txt_tipValueDisplay, txt_splitBill, txt_tipAmt, txt_div1, txt_div2,
            txt_total, txt_amtPerPerson;
    Spinner spin_numPeople;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tip_calculator);
        //I shoved all the initialization into another method since it was ugly here.
        initWidgets();
    }

    private void initWidgets() {
        //initializes all of the things that we might want to modify
        //also overrides the textchangedlistener to let me clear more things.
        btn_Calculate = (Button)findViewById(R.id.btn_Calculate);
        btn_Clear = (Button)findViewById(R.id.btn_Clear);
        btn_tip10 = (Button)findViewById(R.id.btn_tip10);
        btn_tip15 = (Button)findViewById(R.id.btn_tip15);
        btn_tip20 = (Button)findViewById(R.id.btn_tip20);
        input_initialAmount = (EditText)findViewById(R.id.input_initialAmount);
        chk_AddHST = (CheckBox)findViewById(R.id.chk_AddHST);
        slider_tip = (SeekBar)findViewById(R.id.slider_tip);
        slider_tip.setOnSeekBarChangeListener(this);
        txt_tipValueDisplay = (TextView)findViewById(R.id.txt_tipValueDisplay);
        txt_splitBill = (TextView)findViewById(R.id.txt_splitBill);
        txt_tipAmt = (TextView)findViewById(R.id.txt_tipAmt);
        txt_total = (TextView)findViewById(R.id.txt_total);
        txt_amtPerPerson = (TextView)findViewById(R.id.txt_amtPerPerson);
        spin_numPeople = (Spinner)findViewById(R.id.spin_numPeople);

        //auto generated code for reimplementation. We don't give a toss about
        //any of it besides the onTextChanged. The other two can go and die in
        //a fire or something.
        input_initialAmount.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                resetPriceDisplays();
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });
    }

    /*takes values from edit text, then calculates tip value in a separate variable.
    then it gets the value with tax. after storing all of those into one value it
    checks if we are splitting the bill. if so it divides by the split and rounds it.
    */
    public void Calculate(View view) {
        //TODO: implement Calculate method
        //try to create a double for calculations. Throws an error to the user if we can't
        resetPriceDisplays();
        //declare how everything's going to be formated whether the program likes it or not.
        DecimalFormat roundCents = new DecimalFormat("#.##");
        //all of this method is wrapped up in a try/catch method so that we have no crashes.
        try{
            //gets the initial value from the user's input and works from there.
            double enteredPrice = Double.parseDouble(input_initialAmount.getText().toString());
            String y = spin_numPeople.getSelectedItem().toString();
            //this is the tip amount
            int x = slider_tip.getProgress();
            int splitBill = Integer.parseInt(y);
            double hst = 0.13;
            double tip = Double.valueOf(roundCents.format(x*0.01));
            double finalHST = Double.valueOf(roundCents.format(enteredPrice*hst));
            double finalTip = Double.valueOf(roundCents.format(enteredPrice*tip));
            double totalCost = 0.0;
            double splitCost = 0.0;
            //if the number is valid then we go to calculations.
            if(enteredPrice>0.0){
                //check if we calculate with HST
                if(chk_AddHST.isChecked()){
                    totalCost = Double.valueOf(roundCents.format(enteredPrice+finalHST+finalTip));
                    if(splitBill>1){
                        splitCost = Double.valueOf(roundCents.format(totalCost/splitBill));
                        txt_tipAmt.setText(txt_tipAmt.getText().toString()+finalTip);
                        txt_total.setText(txt_total.getText().toString()+totalCost+" (Tax is: $"+finalHST+")");
                        txt_amtPerPerson.setText((txt_amtPerPerson.getText().toString()+splitCost));

                        txt_tipAmt.setVisibility(View.VISIBLE);
                        txt_total.setVisibility(View.VISIBLE);
                        txt_amtPerPerson.setVisibility(View.VISIBLE);
                    }
                    else{
                        txt_tipAmt.setText(txt_tipAmt.getText().toString()+finalTip);
                        txt_total.setText(txt_total.getText().toString()+totalCost+" (Tax is: $"+finalHST+")");

                        txt_tipAmt.setVisibility(View.VISIBLE);
                        txt_total.setVisibility(View.VISIBLE);
                    }
                }
                //otherwise we disregard tax
                else{
                    totalCost = Double.valueOf(roundCents.format(enteredPrice+finalTip));
                    if(splitBill>1){
                        splitCost = Double.valueOf(roundCents.format(totalCost/splitBill));
                        txt_tipAmt.setText(txt_tipAmt.getText().toString()+finalTip);
                        txt_total.setText(txt_total.getText().toString()+totalCost);
                        txt_amtPerPerson.setText((txt_amtPerPerson.getText().toString()+splitCost));

                        txt_tipAmt.setVisibility(View.VISIBLE);
                        txt_total.setVisibility(View.VISIBLE);
                        txt_amtPerPerson.setVisibility(View.VISIBLE);
                    }
                    else{
                        txt_tipAmt.setText(txt_tipAmt.getText().toString()+finalTip);
                        txt_total.setText(txt_total.getText().toString()+totalCost);

                        txt_tipAmt.setVisibility(View.VISIBLE);
                        txt_total.setVisibility(View.VISIBLE);
                    }
                }

            }
        //otherwise we tell the user that they're a retard and clear the app.
            else{
                invalidEntry(view, "Please enter a value greater than 0");
            }
        }
        catch (Exception e){invalidEntry(view, "You need to enter a value");}
    }

    //my custom popup. It's just a method that makes a toast to shoot up and accepts a custom
    //string. It's only really done this way so the already confusing calculate method is a bit
    //less so.
    public void invalidEntry(View view, String _errorText){
        Context context = getApplicationContext();
        CharSequence text = _errorText;
        int duration = Toast.LENGTH_SHORT;
        Toast toast = Toast.makeText(context, text, duration);
        toast.show();
        //clear set text
        clearAll(view);
    }

    /*goes through everything and clears all of the values. I set it up to call a bunch of
    individual methods so I can clear specific things if/when needed.
    */
    public void clearAll(View view) {
        /*Calls all of the individual clear methods so we can have the app
        * go back to how it was when we started it.*/
        clearSetText();
        resetCheckBox();
        resetSlider();
        resetSpinner();
        resetPriceDisplays();
    }
    /*each method clears an individual component of the app so that I can call them
    * later on if i need to only clear one thing.*/
    public void clearSetText(){
        //clear the user price input
        input_initialAmount.setText("");
    }
    public void resetCheckBox(){
        if(chk_AddHST.isChecked()){
        chk_AddHST.toggle();}
    }
    public void resetSlider(){slider_tip.setProgress(0);
        int _seekValue = slider_tip.getProgress();
        txt_tipValueDisplay.setText(Integer.toString(_seekValue));}
    public void resetSpinner(){
        //set the spinner back down to 1
        spin_numPeople.setSelection(0);
    }
    public void resetPriceDisplays(){
        txt_tipAmt.setText("Tip Amount: $");
        txt_tipAmt.setVisibility(View.INVISIBLE);
        txt_total.setText("Total: $");
        txt_total.setVisibility(View.INVISIBLE);
        txt_amtPerPerson.setText("Per Person: $");
        txt_amtPerPerson.setVisibility(View.INVISIBLE);
    }
    //functionally identical to the resetPriceDisplays method but it specifies a view so I can
    //call it from the main activity easier.
    public void resetViewPriceDisplays(View view){
        resetPriceDisplays();
    }
    //this set of three methods are used for the buttons that set the tips.
    public void setTip10(View view) {
        slider_tip.setProgress(10);
        int _seekValue = slider_tip.getProgress();
        txt_tipValueDisplay.setText(Integer.toString(_seekValue));

    }
    public void setTip15(View view) {
        slider_tip.setProgress(15);
        int _seekValue = slider_tip.getProgress();
        txt_tipValueDisplay.setText(Integer.toString(_seekValue));
    }
    public void setTip20(View view) {
        slider_tip.setProgress(20);
        int _seekValue = slider_tip.getProgress();
        txt_tipValueDisplay.setText(Integer.toString(_seekValue));
    }

    //reimplementation of the seekBar onProgressChanged method, as well as the other
    //two abberations that come with it whether I need them or not.
    @Override
    public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
        resetPriceDisplays();
        int _seekValue = slider_tip.getProgress();
        txt_tipValueDisplay.setText(Integer.toString(_seekValue));
    }

    @Override
    public void onStartTrackingTouch(SeekBar seekBar) {
        resetPriceDisplays();
    }

    @Override
    public void onStopTrackingTouch(SeekBar seekBar) {

    }
}
