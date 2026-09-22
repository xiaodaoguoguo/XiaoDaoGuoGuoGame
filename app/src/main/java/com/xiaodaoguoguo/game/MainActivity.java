package com.xiaodaoguoguo.game;

import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceError;
import android.webkit.WebResourceRequest;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ProgressBar;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private static final String GAME_URL = "https://xiaodaoguoguo.github.io/xdg/";

    private WebView webView;
    private ProgressBar progressBar;
    private LinearLayout errorLayout;
    private Button retryButton;

    private long lastBackPressTime = 0;
    private static final int BACK_PRESS_INTERVAL = 2000; // 2秒内双击退出

    @SuppressLint("SetJavaScriptEnabled")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // 保持屏幕常亮
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        // 全屏沉浸式体验
        enableFullscreenMode();

        setContentView(R.layout.activity_main);

        initViews();
        setupWebView();
        loadGame();
    }

    /**
     * 启用全屏沉浸式模式
     */
    private void enableFullscreenMode() {
        View decorView = getWindow().getDecorView();
        int uiOptions = View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_LAYOUT_STABLE;
        decorView.setSystemUiVisibility(uiOptions);
    }

    /**
     * 初始化视图组件
     */
    private void initViews() {
        webView = findViewById(R.id.webView);
        progressBar = findViewById(R.id.progressBar);
        errorLayout = findViewById(R.id.errorLayout);
        retryButton = findViewById(R.id.retryButton);

        retryButton.setOnClickListener(v -> {
            errorLayout.setVisibility(View.GONE);
            loadGame();
        });
    }

    /**
     * 配置WebView设置
     */
    @SuppressLint("SetJavaScriptEnabled")
    private void setupWebView() {
        WebSettings webSettings = webView.getSettings();

        // 启用JavaScript
        webSettings.setJavaScriptEnabled(true);

        // 启用DOM存储
        webSettings.setDomStorageEnabled(true);

        // 启用数据库
        webSettings.setDatabaseEnabled(true);

        // 允许文件访问
        webSettings.setAllowFileAccess(true);

        // 支持缩放
        webSettings.setSupportZoom(false);
        webSettings.setBuiltInZoomControls(false);

        // 自动适应屏幕
        webSettings.setUseWideViewPort(true);
        webSettings.setLoadWithOverviewMode(true);

        // 缓存策略
        webSettings.setCacheMode(WebSettings.LOAD_DEFAULT);

        // 设置WebViewClient
        webView.setWebViewClient(new GameWebViewClient());

        // 设置WebChromeClient以支持进度条
        webView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onProgressChanged(WebView view, int newProgress) {
                if (newProgress == 100) {
                    progressBar.setVisibility(View.GONE);
                } else {
                    progressBar.setVisibility(View.VISIBLE);
                }
            }
        });
    }

    /**
     * 加载游戏
     */
    private void loadGame() {
        progressBar.setVisibility(View.VISIBLE);
        webView.setVisibility(View.VISIBLE);
        webView.loadUrl(GAME_URL);
    }

    /**
     * 自定义WebViewClient处理页面加载
     */
    private class GameWebViewClient extends WebViewClient {

        @Override
        public void onPageStarted(WebView view, String url, Bitmap favicon) {
            super.onPageStarted(view, url, favicon);
            progressBar.setVisibility(View.VISIBLE);
            errorLayout.setVisibility(View.GONE);
        }

        @Override
        public void onPageFinished(WebView view, String url) {
            super.onPageFinished(view, url);
            progressBar.setVisibility(View.GONE);
        }

        @Override
        public void onReceivedError(WebView view, WebResourceRequest request,
                                    WebResourceError error) {
            super.onReceivedError(view, request, error);
            if (request.isForMainFrame()) {
                progressBar.setVisibility(View.GONE);
                webView.setVisibility(View.GONE);
                errorLayout.setVisibility(View.VISIBLE);
            }
        }

        @Override
        public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
            // 保持在当前WebView内加载
            return false;
        }
    }

    /**
     * 处理返回键：双击退出
     */
    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            long currentTime = System.currentTimeMillis();
            if (currentTime - lastBackPressTime < BACK_PRESS_INTERVAL) {
                super.onBackPressed();
                finish();
            } else {
                lastBackPressTime = currentTime;
                Toast.makeText(this, R.string.exit_confirm, Toast.LENGTH_SHORT).show();
            }
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        enableFullscreenMode();
        if (webView != null) {
            webView.onResume();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (webView != null) {
            webView.onPause();
        }
    }

    @Override
    protected void onDestroy() {
        if (webView != null) {
            webView.destroy();
        }
        super.onDestroy();
    }
}
