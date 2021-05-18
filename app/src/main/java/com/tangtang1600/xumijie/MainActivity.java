package com.tangtang1600.xumijie;

import android.os.Bundle;
import android.app.Activity;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.KeyEvent;
import android.widget.EditText;
import android.widget.TextView;

import com.chaquo.python.Kwarg;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends Activity {


    private Python py;
    private TextView textView1;
    private TextView textView2;
    private EditText editText1;
    private EditText editText2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView1 = findViewById(R.id.textView1);
        textView2 = findViewById(R.id.textView2);
        editText1 = findViewById(R.id.editText1);
        editText2 = findViewById(R.id.editText2);

        initPython();
        if (py == null) {
            py = Python.getInstance();
        }

        translate();


    }


    private void translate() {

        TextWatcher textWatcher = new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                if (String.valueOf(s).isEmpty()) {
                    return;
                }
                PyObject pyObject = py.getModule("Translate")
                        .callAttr("translate", new Kwarg("api", "google"), new Kwarg("content", String.valueOf(s)));
                String result = pyObject.toJava(String.class);
                editText2.setText(result);
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        };

        editText1.addTextChangedListener(textWatcher);

    }


    private void initPython() {
        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
    }


}
