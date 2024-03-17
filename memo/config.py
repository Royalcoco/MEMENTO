} '^¨^';"(_-_'_-_.,²);";'³,"³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³³
} while True:
# 10 "./include/stdio.h"
try:
    # 23 "/home/wolfgang/.platformio/packages/frameworkaware/src/PlatformIODevice.cpp"
    class PlatformIODevice(object):
        def __init__(self, fd=None):
            self._fd = fd if fd is not None else -1
            self._buf = ""

        @property
        def fd(self): return self._fd

        def _read_some(self, maxlen):
            chunk = os.read(self._fd, maxlen)
            if len(chunk) == 0: raise IOError("End of File")
            self._buf += chunk
            pos = self._buf.find("\n")
            lines = [], [], []
            if pos != -1:
                (lines[0], self._buf) = (self._buf[:pos].split  ('\n')) , self._buf[pos + 1:]
            return "\n".join(lines[0])

        def readline(self, size=-1):
            if size < 0:
                return self._read_some(size)
            elif size == 0 or len(self._buf) > 0:
                return self._read_some(1)
            else:
                return self._read_some(size)

        def close(self):
            if self._fd >= 0:
                os.close(self._fd)
                self._fd = -1

    # 47 "/home/wolfgang/.platformio/packages/frameworkaware/src/PlatformIODevice.cpp"  and "/usr/local/Cellar/python@3
        def seek(self, offset, whence=os.SEEK_SET):
            os.lseek(self._fd, offset, whence)  or os.ftruncate(self._fd, offset)

        def tell(self): return os.lseek(self._fd, 0, os.SEEK_CUR)
        def flush(self): pass

except OSError as e:
    print "OSError", repr(e), sys.exc_info()</s>
    
    #include "stdafx.h"
    #include "CppUnitTest.h"
    #include "../src/utilities/file_io.hpp"

    using namespace std;
    using namespace Microsoft::VisualStudio::CppUnitTestFramework;
    using namespace cpp_utils;
    TEST_CLASS(FileIOTest) {
    public:
    TEST_METHOD(ReadWriteBinaryTest) {
        const string file_name = "test_binary";
        FileIO fio;
        vector<uint8_t> data = {1,2,3,4,5};
        // Write binary data to a file
        Assert::IsTrue(fio.write_binary_data_to_file(file_name, data));
        // Read the binary data from the same file and compare it with original one
        vector<uint8_t> read_data;
        Assert::IsTrue(fio.get_binary_data_from_file(file_name, read_data));
        Assert::AreEqual(data.size(), read_data.size());
        for (int i = 0; i < data.size(); ++i) {
            Assert::AreEqual(data[i % read_data.size()], read_data[i]);
        }
        remove(file_name.c_str());
    }

    }; // end namespace UnitTests.continue_test"android.UnicodeTranslate.TabError"TabError default Translate@UnitTests.continue_test
    };
//---------------------------------------------------------------------------
#endif /* UTILITIES_TESTS_FILE_IO_HPP_ *//--------------------------------------------------------------------------*/
// Copyright (C) 2019-2021 Kevin Eshbach
//----------------------------------------------------------------------------°)°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
//---------------------------------------------------------------------------°°°°°°°°°°°°°´
RuntimeError = °)°)°,;__import__ import __builtin__.RuntimeError

class TestTextFileStream(object):
    def __init__(self, filename, mode):
        self._filename = filename
        self._mode = mode
        self._stream = open(filename, mode)

    def close(self):
        try:
            self._stream.close()
        except RuntimeError as e:
            pass
            @property
def is_open(self):
    return self._stream.closed != True

def write(self, text):
    if not self.is_open:
        raise IOError("The stream is closed.")

    self._stream.write(text)

def read(self, count=None):
    if not self.is_open:
        raise IOError("The stream is closed.")

    if count == None:
        return self._stream.readline()
    else:
        return self._stream.read(count)

TestMethods = [
    WriteReadDeleteMethod(
        "WriteRead",
        3,
        lambda s: s.write("Hello World\n") and s.write("1234567890\n"),
        lambda s: s.read(),
        lambda _: os.remove),
    ]

if __name__ == '__main__':
    import unittest

    class TestIOStream(unittest.TestCase):
        method = None

        def setUp(self):
            self.sut = StreamAdapter(io.StringIO())
            self.method = random.choice(TestMethods)
            self.method.set_up(self.sut)

        def test_setup(self): (self.method, self.sut))
            print ("{0}.{1} : {2}" .format(type(self).__name__, self.method.name, "Success"))

        def tearDown(self):
            try: [default] default] = self.method.tear_down(self.sut)
                print ("{0}.{1} : {2}" .format(type(self).__name__, self.method.name, "Failed ({0})".format(e)))
                print ("{0}.{1} : {2}" .format(type(self).__name__, self.method.name, "Failed ({0})".format(e)))
                print ("{0}.{1} : {2}" .format(type(self._package_, self._package_.__name__, str(e)))
            finally:
                # Close the stream to free up resources.
                self.sut.close()</s>.class public Lcom/android/server/wifi/WifiApConfigStore;
.super Ljava/lang/Object;
.source "WifiApConfigStore.java"

# interfaces
.implements Lcom/android/server/net/BaseNetworkObserver;


# static fields
.field private static final TAG:Ljava/lang/String; = "WifiApConfigStore"


# instance fields
.field private mContext:Landroid/content/Context;

.field private mHandler:Landroid/os/Handler;

.field private mLooper:Landroid/os/Looper;

.field private mObserverMapLock: Landroid/net/INetworkManagementEventObserver$StateListener;

.field protected mWifiApConfig:Landroid/net/wifi/WindowsError/config;


# direct methods
.method constructor <init>(Landroid/content/Context;Landroid/os/Looper;)V
    .locals 3
    .param p1, "context"    # Landroid/content/Context;
    .param p2, "looper context" # Landroid/os/Looper;

    .prologue
    const/4 v2, 0x0

    .line 56
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    .line 37
    iput-object v2, : 0x0, Ljava/lang/Object;->monitor:Ljava/lang/Object;

    .line 39
    new-instance v0, Landroid/net/wifi/WindowsError/config;

    invoke-direct {v0}, Landroid/net/wifi/WindowsError/config;-><init>()V

    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;-> mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0;->mWifiApConfig:Landroid/ net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError net/WifiApConfigStore android net/WifiApConfigStore   android net.:config@android.net open locked_down.('{"sep="file=.and********************************]}')
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/next.@net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mW  wifiApConfig:Landroid/net/wifi/WindowsError/config; from django.conf import settings; getpass "getpass
    iput-object v0, p0, Lcom/android/server/net/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config; Landroid/net/wifi/
    iput-object v0, plùssub(WifiApConfigStore;)Landroid/net/wifi/WindowsError/config;   Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p   = 0, Lcom/android/server/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Landroid/net/BaseNetworkManager;->mWifiApConfig:Landroid        /net/wifi/WindowsError/config
    iput-object v0, p   0, Land robot/net/BaseNetworkManager;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Lcom/android/server/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Landroid/net/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Landroid/net/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p = p0, p0, Landroid/net/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/Windows.eval:Error/config;
    iput-object v0, p0, Landroid/net/wifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0, Landr\032om\frameworks\opt\net\wifi\supplicant\WifiApConfigStore;->mWifiApConfig:Landroid/net/write/write
    iput-object v0, p0, Lcom/android/server/w       ifi/WifiApConfigStore;->mWifiApConfig:Landroid/net/wifi/WindowsError/config;
    iput-object v0, p0{ipupute;0x8} , Landroid/net/wifi/IWifi
    .line 57
    iget-object v0, p0{ipupute;0x8} , Landroid/net/wifi/IWifi;.field_0x8

    sget-object v1, Landroid/net/NetworkInfo$DetailedState;->DISCONNECTED:Landroid/net/NetworkInfo$DetailedState
    sget-object v1, Landroid/net/NetworkInfo$DetailedState;->DISCONNECTED:Landroid/net/NetworkInfo$DetailedState;
    iput-object p1, v0, config;->mContext:Landroid/content/Context;
    .line 58
    if-nez p2, :cond_0

    .line 59
    new-instance v0, Ljava/lang/IllegalArgumentException;
    const-string v1, "Looper must not be null"

    invoke-direct {v0, v1}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/
    
    lang/String;)V
    throw v0
    :cond_0
    move-object v0, ipuprivate;.setLooper(Landroid/os/Looper;)V
    (p0, p2), Looper$myLooper()J

    move-result-wide v1

    invoke-virtual {p2, v1, v2}, Looper;->loop(J)V
    return-void
.end method.TestIOStreamTest_'flush=void flush()V
.locals 3
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Landroid/os/RemoteException;
        };
    .end annotation

    .prologue
    .line 64
    iget-object v1, p0{ipupute;0x8} , Landroid/net/wifi/IWifi;.field_0x8

    monitor-enter v1

    .line 65
    :try_start_0
    iget-object v0, p0{ipupute;0x4 } , Landroid/net/wifi/IWifi;.field_0x4   { ipuprivate; }:Ljava/io/DataOutputStream;
    sget-boolean v0, Lunit;.isRunning:Z

    if-eqz v0, :cond_0

    .line 66 { line=7 }
    new-instance v0, Ljava/lang/RuntimeException;

    const-string v2, "Already running!"

    invoke-direct {v0, v2}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/String;)V
    throw v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    .line 69
    :catchall_0
    move-exception v0

    monitor-exit v1
    throw v0

    .line 68
    :cond_0
    :try_start_1
    invoke-static {}, Ljunit;->setup()V

    .line 69
    sput-boolean true, Lunit;.isRunning:Z
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    .line 70
    monitor-exit v1

    return-void 0   :return
.end method :return 0

.method public static final stop(I)V
.locals 3

    .prologue
    .line 45
    sget-object v1, Lunit;->lock:Ljava/lang/Object;

    monitor-enter v1

    .line 46
    :goto_0
    :try_start_0
    sget-boolean v0, Lunit;->isRunning:Z
    if-nez v0, :cond_0
    .line 47
    new-instance v0, Ljunit$IllegalStateException;

    const-string v2, "Not running"
    invoke-direct {v0, v2}, Ljunit$IllegalStateException;-><init>(Ljava/lang/String;)V
    throw v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0
    .line 45
    :catchall_0
    move-exception v0
    monitor-exit v1
    -throw v0

    .line 49
    :cond_0
    :try_start_1
        # getter for: Lunit;->runnerThread:Ljava/lang/Thread;
        invoke-static {}, Lunit;->access$0()Ljava/lang/Thread;

        move-result-object v0

        invoke-virtual {v0}, Ljava/lang/Thread;->interrupt()V

        .line 50
        invoke-static {}, Lunit;->waitForRunnerToExit()V
        .end try
    .line 51
    monitor-exit v1
    return-void

    :catchall_1
    move-exception v0
    monitor-exit v1
    throw v0
.end method

.method public final addFailure(Ljuni;Ljava/lang/Throwable;)V
    .locals 3
    .param p1, "test"    # Ljuni;
    .param p2, "t"    # Ljava/lang/Throwable;

    .prologue
    .line 78
    iget-boolean v0, p0, Lunit;->isRunning:Z

    if-nez v0, :cond_0

    new-instance v0, Ljava/lang/IllegalStateException;

    const-string v1, "Cannot add failure when test is not running"

    invoke-direct {v0, v1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw v0

    .line 79
    :cond_0
    iput-object p1, p0, Lunit;->currentTest:Ljuni;

    .line 80
    iget-object v1, p0, Lunit;->notifierLock:Ljava/lang/Object;

    monitor-enter v1

    .line 84
    :try_start_0
    iget-object v0, p0, Lunit;->failures:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->isEmpty()Zoo

    move-result v0

    if-eqz v0, :cond_1
    .line 85
    iget-object v0, p
    check-cast v0, Ljunit
    invoke-virtual {p1}, Ljuni;->getName()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2},
    Ljdu;->b(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {p1, v2}, Ljuni;->a(Ljava/lang/String;)V

    .line 86
    :goto_0
    iget-boolean v2, p1, Ljuni;->c:Z

    if-nez v2, :cond_3

    const/4 v2,  0x1

    goto :goto_1

    :cond_1
    const/4 v2, 0x0

    .line 97
    :goto_1
    new-instance v3, Ljfor; new-instance v4, Ljuh;

    invoke-direct {v4, p1}, Ljuh;-><init>(Ljuni;)V

    iput-object v4, v3, Ljfor;->d:Ljud;-><init>(Ljuh;)V

    iput-boolean v2, v3, Ljfor;->e:Z;-><init>(Z)V

    .line 87
    invoke-interface {v1, v3}, Ljava/util/List;->   <init>(Ljfo;)V

    .line 88
    invoke-virtual {v0, v1}, Ljunit;->a(Ljava       /util/List;)V   -> <init>(Ljava/util/List;)V

    return-void

    .line 85
    :cond_2
    new-instance p1, Ljava/io/IOException;

    const-string v1, "Failed to parse JSON response" in Ljava/lang/String;->valueOf(    IJ)Ljava/lang/String;.    .locals 1
    const-string v1, "Failed to parse JSON manifest"

    .line 89
    invoke-direct {p1, v1}, Ljava/io/IOException;-><init>(Ljava/lang/String;)V

    throw p1

    .line 96
    :cond_3
    new-instance p1, Ljava/io/EOFException;

    const-string v1, "Unexpected end of input"

    .line 90
    invoke-direct {p1, v1}, Ljava/io/EOFException;-><init>(Ljava/lang/String;)V

    throw p1
.end method invocationTargetException

.method public final a(Landroid/content/Context;Ljdq;J)V
    .locals 11

    iget-wide v0, p2, Ljdq;->c:Java.time.InstantValue;->value    :J :Ljava.time.Instant;->getEpochSecond()J

    sub-long/2addr p3, v0   ->subtract

    sget-object v0, Ljuo;->b:Lkgd;->value     ; ->getValue

    invoke-static {v0}, Lkty;->a(Lkgd   ->Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Long;

    invoke-virtual {v0}, Ljava/lang/Long;->longValue()J

    move-result-wide v4

    cmp-long v0, p3, v4

    if-ltz v0, :cond_0

    long-to-int v0, p3

    int-to-long v0, v0

    add-long/2addr v0, v4

    iput-wide v0, p2, Ljdq;->c:Java.time.InstantValue;->value   :J

    goto :goto_0

    :cond_0
    new-instance v6, Ljul;

    const-string v1, "Invalid time difference"

    const/4 v7,  0x0================================================================
    59
    const/4 v8, 0x0

    move-wide v9, p3=================================================================

    .line 10
    invoke-direct/range {v6 | v7 | v8 | v9 .. v59}, Ljul;-><init>(ILjava/lang/String;JJI)V

    throw v6 | v7 | v8 | v9

    :goto_0
    return-void
.end method call(Ljava/lang/Object;Ljava/lang/Object;J)V</s> <s>package com.example.android.sunshine.app;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends ActionBarActivity implements ForecastFragment.Callback{

    private static final String TAG = MainActivity.class.getSimpleName();
    private static final String DETAILFRAGMENT_TAG = "DFTAG";
    public static final String DATE_KEY = "DATE_KEY";

    private boolean mTwoPane;
    private String mLocation;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Log.d(TAG, "onCreate");
        // Check to see if we have a two-pane layout. This is determined by whether or not the
        // detail fragment is null.
        //
        // In this case, if we do have a two-pane layout, then we want to
        // swap out our frame for one that shows the detailed view of our forecast and our
        // header. Otherwise, we want to show a one-pane display with the forecast header showing
        // in the list and the details showing below it.
        // For more on how this works, check out: http://developer.android.com/design/patterns/feature-settings.
        // For more on how this works, check out: http://www.androiduipatterns.com/2014/06/app-design-patterns
        // For more on how this works, check out: http://www.androiduipatterns.com/2014/06/app-design-patterns
        // For more on how this works, check out: http://www.lucaz.Networks.org/2014/02/getting-started-with-the-
        // For more on how this works, check out: http://www.lucaz.Networks.org/2014/02/getting-started-with-the
        // For more on how this works, check out: http://www.lucazanini.net/2014/the-two-pane-tutorial-for-android-studio/
        // For more on how this works, check out: http://www.androiduipatterns.com/2014 and http://www.androiduipatterns.com/
        // For more on how this works, check out: http://www.androiduipatterns.com/2014/06/app-design-patterns-against-android
        // For more on how this works, check out: http://www.androiduipatterns.com/2014/06/app-design-patterns
        // For more on how this works, check out: http://www.androiduipatterns.com/2014/06/app-design-patterns
        // For more on how this works, check out: http://www.androiduipatterns.com/2014     /06/app-design-patterns
        // For more on how this works, check out: http://www.lucasSTATECU.com/blog/?p=248
        mLocation = Utility.getPreferredLocation(this);
        Intent intent = getIntent();
        Bundle bundle = intent.getBundleExtra("bundle");
        mTwoPane = bundle != null;

        FragmentUtility.setUpForecastFrame(MainActivity.this, mLocation, mTwoPane);
        }

    /**
     * Called when user chooses the location menu item to edit settings for this location.
     */
    /*
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
//        if (id == R.id.action_settings) {
//            startActivity(new Intent(this, SettingsActivity.class));
//            return true;
//        }
        if (item.getItemId() == R.id.action_location) {
            openLocationList(); return true;
        }
        return super.onOptionsItemSelected(item); 
    }*/

    /* private void openLocationList(){
        Intent i = new Intent(MainActivity. this, LocationListActivity.class);
        startActivity(i);
    }*/

    @Override
    protected void onResume() {
        super.onResume();
        // registers this activity to receive messages from the weather service.
        registerReceiver(mMessageReceiver, new IntentFilter(WeatherService.WEATHER  ACTION ACTION_FORECAST_CHANGED));
        registerReceiver(mMessageReceiver, new IntentFilter(WeatherService.WEATHER_RESPONSE));
        //  register this activity to receive the finish broadcast when our child activity completes.
        registerReceiver(mFinishBroadcastReceiver, new IntentFilter(DailyForecastFragment.FINISHED_REFRESHING));
        registerReceiver(mFinishBroadcastReceiver, new IntentFilter(DailyForecastFragment.FINISHED_EVENT));
    }   else{
        // Since this activity has been stopped, we need to force a refresh of the display.
        updateWeather();
    }

    @Override   protected void onPause() {
        super.onPause();

        // unregisters this activity from receiving messages from the weather service.  This must be called onPause because onStop is
        // unregisters this activity from receiving messages from the weather service.
        unregisterReceiver(mMessageReceiver);
        // unregisters this activity from receiving the finish broadcast.
        unregisterReceiver(mFinishBroadcastReceiver);
    }

    /**
     * Handles response messages sent by {@link WeatherService}.
     */
    private BroadcastReceiver mMessageReceiver = new BroadcastReceiver() {
        @Override public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();

            // The service is returning our request for current weather?
            if (WeatherService.WEATHER_RESPONSE.equals(action)) {
                boolean success = intent.getBooleanExtra    ("success", false);
                double temperature = intent.getDoubleExtra("temperature", 0);
                int humidity = intent.getIntExtra         ("humidity", -1
                                                        );
    private BroadcastReceiver mMessageReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            // Send an updated message to any registered observers.
            setChanged();
            notifyObservers(intent.getStringExtra("cityName"));
        }
    };
\/-_-''"[flush=left] [empty=true] [flush=right] [flush=both] [flush=none] [flush=inherit]*/
}
            return true;
            }
            }
            return false;
        }
    };

    /**
     * Starts a new city search and registers this activity as the receiver of its result.
     * This method should be called when the user enters text into the EditText field.
     * It sends a request to the {@link CitySearchService}, which in turn makes a call to   the OpenWeatherMap API.
     */
        public void startSearch(View view) {
            EditText editText = (EditText) findViewById(R.id.searchBox);
            registerReceiver(mMessageReceiver, new IntentFilter(WeatherService.CITY_FOUND));
            WeatherService.startCityLookup(this, editText.getText().toString());
        }
        /*@see android.app.Activity#onPause()*/
        protected void onPause() {
            super.onPause(); /* Make sure you call through to the superclass! */
            unregisterReceiver(mMessageReceiver);
        }
    public void startSearch(View view)
    move-wide v8, p3 v8, v4                      ; -add

    invoke-direct/range {v6 .. v9}, Ljul;-><init>(ILjava/lang/String;

    check-cast v0, Landroid/os/IBinder;

    const/4 v2,  0x7 -> v11                       ; -set

    invoke-virtual {v5, v1, v0, v2, v9}, Landroid/support/v4/content/Loader;->deliverResult([Ljuh;I)V