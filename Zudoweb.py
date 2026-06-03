<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>ZUDOOTP - Premium Store</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  /* ============ RESET & BASE ============ */
  *{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif;}
  :root{
    --bg-1:#0f0c29;
    --bg-2:#302b63;
    --bg-3:#24243e;
    --neon:#00e5ff;
    --neon-2:#ff00e5;
    --gold:#ffd700;
    --green:#00ff88;
    --red:#ff3860;
    --card:rgba(255,255,255,0.06);
    --card-border:rgba(255,255,255,0.12);
    --text:#fff;
    --text-dim:#b8b8d4;
  }
  body{
    min-height:100vh;
    background:linear-gradient(135deg,var(--bg-1),var(--bg-2),var(--bg-3));
    background-size:400% 400%;
    animation:bgShift 15s ease infinite;
    color:var(--text);
    overflow-x:hidden;
  }
  @keyframes bgShift{
    0%,100%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
  }
  /* ============ FLOATING PARTICLES ============ */
  .particles{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;}
  .particle{position:absolute;border-radius:50%;background:radial-gradient(circle,var(--neon),transparent);opacity:0.4;animation:float linear infinite;}
  @keyframes float{
    0%{transform:translateY(100vh) scale(0);opacity:0;}
    10%{opacity:0.4;}
    90%{opacity:0.4;}
    100%{transform:translateY(-10vh) scale(1.2);opacity:0;}
  }

  /* ============ AUTH SCREEN ============ */
  .auth-wrap{
    position:fixed;inset:0;display:flex;align-items:center;justify-content:center;
    z-index:100;padding:20px;
  }
  .auth-card{
    background:var(--card);backdrop-filter:blur(20px);
    border:1px solid var(--card-border);border-radius:24px;
    padding:40px 32px;width:100%;max-width:420px;
    box-shadow:0 20px 60px rgba(0,0,0,0.5),0 0 80px rgba(0,229,255,0.15);
    animation:authIn .6s ease;
  }
  @keyframes authIn{from{opacity:0;transform:translateY(30px) scale(.95);}to{opacity:1;transform:none;}}
  .logo{
    text-align:center;margin-bottom:28px;
  }
  .logo-icon{
    width:80px;height:80px;margin:0 auto 12px;border-radius:24px;
    background:linear-gradient(135deg,var(--neon),var(--neon-2));
    display:flex;align-items:center;justify-content:center;font-size:42px;
    box-shadow:0 10px 30px rgba(0,229,255,0.4);
    animation:pulse 2s ease infinite;
  }
  @keyframes pulse{0%,100%{transform:scale(1);}50%{transform:scale(1.05);}}
  .logo h1{
    font-size:28px;font-weight:800;
    background:linear-gradient(135deg,var(--neon),var(--neon-2));
    -webkit-background-clip:text;background-clip:text;color:transparent;
    letter-spacing:2px;
  }
  .logo p{color:var(--text-dim);font-size:13px;margin-top:4px;}
  .tab-row{
    display:flex;background:rgba(0,0,0,0.3);border-radius:12px;padding:4px;margin-bottom:24px;
  }
  .tab{
    flex:1;padding:10px;text-align:center;border-radius:8px;cursor:pointer;
    font-weight:600;font-size:14px;color:var(--text-dim);transition:.3s;
  }
  .tab.active{
    background:linear-gradient(135deg,var(--neon),var(--neon-2));color:#000;
  }
  .field{margin-bottom:16px;}
  .field label{display:block;font-size:12px;font-weight:600;color:var(--text-dim);margin-bottom:6px;text-transform:uppercase;letter-spacing:1px;}
  .field input{
    width:100%;padding:14px 16px;background:rgba(0,0,0,0.4);
    border:1px solid var(--card-border);border-radius:12px;
    color:#fff;font-size:15px;outline:none;transition:.3s;
  }
  .field input:focus{border-color:var(--neon);box-shadow:0 0 0 3px rgba(0,229,255,0.15);}
  .btn-primary{
    width:100%;padding:14px;border:none;border-radius:12px;
    background:linear-gradient(135deg,var(--neon),var(--neon-2));
    color:#000;font-weight:700;font-size:15px;cursor:pointer;
    transition:.3s;letter-spacing:1px;
    box-shadow:0 8px 24px rgba(0,229,255,0.3);
  }
  .btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 32px rgba(0,229,255,0.5);}
  .auth-msg{
    margin-top:14px;padding:10px;border-radius:10px;font-size:13px;text-align:center;
    display:none;
  }
  .auth-msg.error{background:rgba(255,56,96,0.15);color:var(--red);border:1px solid var(--red);display:block;}
  .auth-msg.ok{background:rgba(0,255,136,0.15);color:var(--green);border:1px solid var(--green);display:block;}

  /* ============ MAIN APP ============ */
  .app{display:none;min-height:100vh;position:relative;z-index:1;}
  .app.show{display:block;}
  header{
    padding:18px 24px;display:flex;justify-content:space-between;align-items:center;
    background:rgba(0,0,0,0.3);backdrop-filter:blur(15px);
    border-bottom:1px solid var(--card-border);position:sticky;top:0;z-index:50;
  }
  .brand{display:flex;align-items:center;gap:12px;}
  .brand .logo-icon{width:44px;height:44px;font-size:22px;margin:0;border-radius:12px;animation:none;}
  .brand h2{font-size:18px;font-weight:700;letter-spacing:1px;}
  .brand h2 span{background:linear-gradient(135deg,var(--neon),var(--neon-2));-webkit-background-clip:text;background-clip:text;color:transparent;}
  .header-right{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
  .balance-pill{
    padding:8px 14px;border-radius:20px;font-weight:600;font-size:14px;
    background:linear-gradient(135deg,rgba(255,215,0,0.2),rgba(255,215,0,0.05));
    border:1px solid var(--gold);color:var(--gold);
  }
  .icon-btn{
    width:38px;height:38px;border-radius:10px;background:var(--card);
    border:1px solid var(--card-border);display:flex;align-items:center;justify-content:center;
    cursor:pointer;transition:.3s;font-size:16px;
  }
  .icon-btn:hover{background:var(--neon);color:#000;}

  .container{padding:24px;max-width:1200px;margin:0 auto;}
  .hero{
    background:linear-gradient(135deg,rgba(0,229,255,0.1),rgba(255,0,229,0.08));
    border:1px solid var(--card-border);border-radius:20px;padding:28px;margin-bottom:24px;
    position:relative;overflow:hidden;
  }
  .hero::before{
    content:'';position:absolute;top:-50%;right:-20%;width:400px;height:400px;
    background:radial-gradient(circle,rgba(0,229,255,0.2),transparent 70%);
  }
  .hero h1{font-size:26px;margin-bottom:8px;position:relative;}
  .hero p{color:var(--text-dim);position:relative;font-size:14px;}
  .wallet-big{
    margin-top:16px;font-size:32px;font-weight:800;position:relative;
    background:linear-gradient(135deg,var(--gold),#ff9d00);
    -webkit-background-clip:text;background-clip:text;color:transparent;
  }

  .menu-grid{
    display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px;
  }
  .menu-card{
    background:var(--card);border:1px solid var(--card-border);
    backdrop-filter:blur(10px);border-radius:16px;padding:20px;
    cursor:pointer;transition:.3s;text-align:center;position:relative;overflow:hidden;
  }
  .menu-card::before{
    content:'';position:absolute;inset:0;
    background:linear-gradient(135deg,var(--neon),var(--neon-2));
    opacity:0;transition:.3s;z-index:0;
  }
  .menu-card:hover{transform:translateY(-4px);border-color:var(--neon);box-shadow:0 12px 28px rgba(0,229,255,0.2);}
  .menu-card:hover::before{opacity:0.15;}
  .menu-card > *{position:relative;z-index:1;}
  .menu-icon{font-size:36px;margin-bottom:10px;}
  .menu-card h3{font-size:14px;font-weight:600;}
  .menu-card.owner{border-color:var(--gold);background:linear-gradient(135deg,rgba(255,215,0,0.1),transparent);}

  /* ============ PAGES ============ */
  .page{display:none;animation:fadeIn .4s ease;}
  .page.active{display:block;}
  @keyframes fadeIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
  .page-head{
    display:flex;align-items:center;gap:12px;margin-bottom:20px;
  }
  .back-btn{
    width:40px;height:40px;border-radius:10px;background:var(--card);
    border:1px solid var(--card-border);display:flex;align-items:center;justify-content:center;
    cursor:pointer;transition:.3s;font-size:18px;
  }
  .back-btn:hover{background:var(--neon);color:#000;}
  .page-head h2{font-size:22px;font-weight:700;}

  /* ============ COUNTRY CARDS ============ */
  .country-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;}
  .country-card{
    background:var(--card);border:1px solid var(--card-border);border-radius:16px;
    padding:18px;cursor:pointer;transition:.3s;
  }
  .country-card:hover{transform:translateY(-3px);border-color:var(--neon);}
  .country-flag{font-size:42px;margin-bottom:8px;}
  .country-card h4{font-size:16px;margin-bottom:6px;}
  .country-meta{display:flex;justify-content:space-between;font-size:12px;color:var(--text-dim);margin-top:8px;}
  .country-meta .price{color:var(--gold);font-weight:700;}
  .country-meta .stock{color:var(--green);font-weight:600;}

  /* ============ FORMS / DETAILS ============ */
  .detail-card{
    background:var(--card);border:1px solid var(--card-border);border-radius:16px;padding:24px;
    max-width:520px;margin:0 auto;
  }
  .detail-card h3{font-size:20px;margin-bottom:6px;}
  .detail-row{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px dashed var(--card-border);font-size:14px;}
  .detail-row span:last-child{color:var(--neon);font-weight:600;}
  .actions{display:flex;gap:10px;margin-top:18px;flex-wrap:wrap;}
  .actions button{flex:1;min-width:140px;}
  .btn{
    padding:12px 18px;border:none;border-radius:10px;cursor:pointer;
    font-weight:600;font-size:14px;transition:.3s;
  }
  .btn-neon{background:linear-gradient(135deg,var(--neon),var(--neon-2));color:#000;}
  .btn-gold{background:linear-gradient(135deg,var(--gold),#ff9d00);color:#000;}
  .btn-green{background:linear-gradient(135deg,#00ff88,#00b86b);color:#000;}
  .btn-red{background:linear-gradient(135deg,var(--red),#c0224b);color:#fff;}
  .btn-ghost{background:rgba(255,255,255,0.06);color:#fff;border:1px solid var(--card-border);}
  .btn:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(0,0,0,0.3);}

  /* ============ TOAST ============ */
  .toast-wrap{position:fixed;top:20px;right:20px;z-index:9999;display:flex;flex-direction:column;gap:10px;}
  .toast{
    padding:14px 18px;border-radius:12px;background:rgba(0,0,0,0.85);
    backdrop-filter:blur(10px);border-left:4px solid var(--neon);
    color:#fff;min-width:240px;max-width:340px;font-size:14px;
    box-shadow:0 10px 30px rgba(0,0,0,0.5);animation:toastIn .3s ease;
  }
  .toast.ok{border-color:var(--green);}
  .toast.err{border-color:var(--red);}
  .toast.warn{border-color:var(--gold);}
  @keyframes toastIn{from{transform:translateX(120%);}to{transform:none;}}

  /* ============ MODAL ============ */
  .modal-bg{
    position:fixed;inset:0;background:rgba(0,0,0,0.7);backdrop-filter:blur(8px);
    display:none;align-items:center;justify-content:center;z-index:200;padding:20px;
  }
  .modal-bg.show{display:flex;}
  .modal{
    background:linear-gradient(135deg,var(--bg-2),var(--bg-3));
    border:1px solid var(--card-border);border-radius:20px;
    padding:28px;width:100%;max-width:460px;animation:authIn .3s;
  }
  .modal h3{margin-bottom:14px;font-size:20px;}
  .modal .field{margin-bottom:14px;}

  /* ============ OWNER PANEL ============ */
  .owner-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px;}
  .stat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:14px;margin-bottom:20px;}
  .stat{
    background:var(--card);border:1px solid var(--card-border);border-radius:14px;padding:18px;
  }
  .stat .lbl{font-size:12px;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px;}
  .stat .val{font-size:24px;font-weight:800;margin-top:4px;
    background:linear-gradient(135deg,var(--neon),var(--neon-2));
    -webkit-background-clip:text;background-clip:text;color:transparent;
  }

  /* ============ LISTS ============ */
  .list-item{
    background:var(--card);border:1px solid var(--card-border);border-radius:12px;
    padding:14px;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;gap:10px;
  }
  .list-item .info{flex:1;}
  .list-item .info b{display:block;margin-bottom:4px;}
  .list-item .info small{color:var(--text-dim);}

  /* ============ HISTORY ============ */
  .history-card{
    background:var(--card);border:1px solid var(--card-border);border-radius:14px;padding:16px;margin-bottom:10px;
  }
  .history-card .top{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;}
  .history-card .top b{color:var(--neon);}
  .history-card .top .amt{color:var(--gold);font-weight:700;}

  /* ============ DEPOSIT QR ============ */
  .qr-box{
    background:#fff;padding:16px;border-radius:14px;text-align:center;margin-bottom:14px;
  }
  .qr-box img{width:100%;max-width:240px;}
  .upi-info{
    background:rgba(0,0,0,0.4);padding:12px;border-radius:10px;text-align:center;
    font-family:monospace;color:var(--neon);margin-bottom:14px;
  }

  .empty{
    padding:40px 20px;text-align:center;color:var(--text-dim);
  }
  .empty .ic{font-size:60px;margin-bottom:10px;}

  /* responsive */
  @media (max-width:600px){
    .hero h1{font-size:22px;}
    .wallet-big{font-size:26px;}
    .container{padding:16px;}
    header{padding:14px 16px;}
    .brand h2{font-size:15px;}
    .balance-pill{font-size:12px;padding:6px 10px;}
  }
</style>
</head>
<body>

<!-- ===== Floating particles ===== -->
<div class="particles" id="particles"></div>

<!-- ===== Toast container ===== -->
<div class="toast-wrap" id="toastWrap"></div>

<!-- ============ AUTH SCREEN ============ -->
<div class="auth-wrap" id="authScreen">
  <div class="auth-card">
    <div class="logo">
      <div class="logo-icon">⚡</div>
      <h1>ZUDOOTP</h1>
      <p>Premium Digital Store</p>
    </div>
    <div class="tab-row">
      <div class="tab active" id="tabLogin" onclick="switchTab('login')">🔐 Login</div>
      <div class="tab" id="tabReg" onclick="switchTab('reg')">✨ Register</div>
    </div>

    <!-- Login form -->
    <div id="loginForm">
      <div class="field">
        <label>Username</label>
        <input type="text" id="loginUser" placeholder="Enter username" autocomplete="off"/>
      </div>
      <div class="field">
        <label>Password</label>
        <input type="password" id="loginPass" placeholder="Enter password"/>
      </div>
      <button class="btn-primary" onclick="doLogin()">🚀 LOGIN</button>
    </div>

    <!-- Register form -->
    <div id="regForm" style="display:none;">
      <div class="field">
        <label>Choose Username</label>
        <input type="text" id="regUser" placeholder="e.g. zudo_user" autocomplete="off"/>
      </div>
      <div class="field">
        <label>Create Password</label>
        <input type="password" id="regPass" placeholder="Min 4 characters"/>
      </div>
      <div class="field">
        <label>Confirm Password</label>
        <input type="password" id="regPass2" placeholder="Re-enter password"/>
      </div>
      <button class="btn-primary" onclick="doRegister()">✨ CREATE ACCOUNT</button>
    </div>

    <div class="auth-msg" id="authMsg"></div>
  </div>
</div>

<!-- ============ MAIN APP ============ -->
<div class="app" id="app">
  <header>
    <div class="brand">
      <div class="logo-icon">⚡</div>
      <h2><span>ZUDOOTP</span> Store</h2>
    </div>
    <div class="header-right">
      <div class="balance-pill" id="balancePill">💎 ₹0.00</div>
      <div class="icon-btn" title="Owner Panel" onclick="openOwnerPanel()">👑</div>
      <div class="icon-btn" title="Logout" onclick="doLogout()">🚪</div>
    </div>
  </header>

  <div class="container">
    <!-- HOME PAGE -->
    <div class="page active" id="page-home">
      <div class="hero">
        <h1>👋 Welcome, <span id="heroUser">User</span></h1>
        <p>Your one-stop shop for premium digital assets. Buy accounts, sessions, services & more.</p>
        <div class="wallet-big" id="walletBig">💎 ₹0.00</div>
      </div>

      <div class="menu-grid">
        <div class="menu-card" onclick="goto('accounts')">
          <div class="menu-icon">🛒</div>
          <h3>Buy Account</h3>
        </div>
        <div class="menu-card" onclick="toast('🚧 Coming Soon!','warn')">
          <div class="menu-icon">📱</div>
          <h3>Get Sessions</h3>
        </div>
        <div class="menu-card" onclick="goto('profile')">
          <div class="menu-icon">👤</div>
          <h3>Profile</h3>
        </div>
        <div class="menu-card" onclick="goto('deposit')">
          <div class="menu-icon">💰</div>
          <h3>Deposit</h3>
        </div>
        <div class="menu-card" onclick="toast('🆘 Contact: @lTZ_ME_ADITYA_02','warn')">
          <div class="menu-icon">🆘</div>
          <h3>Support</h3>
        </div>
        <div class="menu-card" onclick="toast('🎁 Coming Soon!','warn')">
          <div class="menu-icon">🎁</div>
          <h3>Refer & Earn</h3>
        </div>
        <div class="menu-card" onclick="goto('server2')">
          <div class="menu-icon">🚀</div>
          <h3>Server 2</h3>
        </div>
        <div class="menu-card" onclick="goto('history')">
          <div class="menu-icon">📊</div>
          <h3>History & Stats</h3>
        </div>
      </div>
    </div>

    <!-- ACCOUNTS PAGE -->
    <div class="page" id="page-accounts">
      <div class="page-head">
        <div class="back-btn" onclick="goto('home')">←</div>
        <h2>🌍 Available Accounts</h2>
      </div>
      <div id="countryList" class="country-grid"></div>
    </div>

    <!-- COUNTRY DETAIL -->
    <div class="page" id="page-country">
      <div class="page-head">
        <div class="back-btn" onclick="goto('accounts')">←</div>
        <h2 id="cdTitle">Country</h2>
      </div>
      <div class="detail-card" id="cdBody"></div>
    </div>

    <!-- PROFILE -->
    <div class="page" id="page-profile">
      <div class="page-head">
        <div class="back-btn" onclick="goto('home')">←</div>
        <h2>👤 My Profile</h2>
      </div>
      <div class="detail-card" id="profileBody"></div>
    </div>

    <!-- DEPOSIT -->
    <div class="page" id="page-deposit">
      <div class="page-head">
        <div class="back-btn" onclick="goto('home')">←</div>
        <h2>💰 Add Funds</h2>
      </div>
      <div class="detail-card">
        <h3>Choose Method</h3>
        <p style="color:var(--text-dim);margin-bottom:14px;">Minimum deposit: ₹1</p>
        <div class="actions">
          <button class="btn btn-neon" onclick="goto('depositUPI')">💸 UPI Payment</button>
          <button class="btn btn-gold" onclick="goto('coupon')">🎟 Coupon Code</button>
        </div>
      </div>
    </div>

    <!-- DEPOSIT UPI -->
    <div class="page" id="page-depositUPI">
      <div class="page-head">
        <div class="back-btn" onclick="goto('deposit')">←</div>
        <h2>💸 UPI Deposit</h2>
      </div>
      <div class="detail-card">
        <h3>Step 1: Enter Amount</h3>
        <div class="field" style="margin-top:14px;">
          <label>Amount (INR)</label>
          <input type="number" id="depAmount" placeholder="Min ₹1" min="1"/>
        </div>
        <button class="btn btn-neon" style="width:100%;" onclick="genQR()">Generate QR ➜</button>
        <div id="qrZone" style="display:none;margin-top:18px;">
          <div class="qr-box">
            <img id="qrImg" alt="QR"/>
          </div>
          <div class="upi-info">UPI: fearlessaditya@fam</div>
          <p style="font-size:13px;color:var(--text-dim);margin-bottom:14px;text-align:center;">
            Pay via any UPI app, then submit your UTR/Txn ID below.
          </p>
          <div class="field">
            <label>UTR / Transaction ID</label>
            <input type="text" id="depUTR" placeholder="Enter UTR or Txn ID"/>
          </div>
          <button class="btn btn-green" style="width:100%;" onclick="submitDeposit()">✅ Submit for Auto-Approve</button>
        </div>
      </div>
    </div>

    <!-- COUPON -->
    <div class="page" id="page-coupon">
      <div class="page-head">
        <div class="back-btn" onclick="goto('deposit')">←</div>
        <h2>🎟 Redeem Coupon</h2>
      </div>
      <div class="detail-card">
        <div class="field">
          <label>Coupon Code</label>
          <input type="text" id="couponInput" placeholder="Enter coupon code" style="text-transform:uppercase;"/>
        </div>
        <button class="btn btn-gold" style="width:100%;" onclick="redeemCoupon()">🎁 REDEEM</button>
      </div>
    </div>

    <!-- HISTORY -->
    <div class="page" id="page-history">
      <div class="page-head">
        <div class="back-btn" onclick="goto('home')">←</div>
        <h2>📊 History & Stats</h2>
      </div>
      <div id="historyBody"></div>
    </div>

    <!-- SERVER 2 -->
    <div class="page" id="page-server2">
      <div class="page-head">
        <div class="back-btn" onclick="goto('home')">←</div>
        <h2>🚀 Server 2 - Marketplace</h2>
      </div>
      <div class="detail-card" style="margin-bottom:18px;">
        <p style="font-size:13px;color:var(--text-dim);">
          ⚠️ <b>Disclaimer:</b> This server only connects buyers and sellers. Owner is NOT responsible for any scams.
        </p>
      </div>
      <div class="actions" style="margin-bottom:18px;">
        <button class="btn btn-neon" onclick="goto('srvList')">✅ Available Services</button>
        <button class="btn btn-gold" onclick="goto('srvAdd')">➕ Add Service (₹10 Fee)</button>
      </div>
    </div>

    <!-- SERVICE LIST -->
    <div class="page" id="page-srvList">
      <div class="page-head">
        <div class="back-btn" onclick="goto('server2')">←</div>
        <h2>🛍 Available Services</h2>
      </div>
      <div id="srvListBody"></div>
    </div>

    <!-- SERVICE ADD -->
    <div class="page" id="page-srvAdd">
      <div class="page-head">
        <div class="back-btn" onclick="goto('server2')">←</div>
        <h2>➕ Add New Service</h2>
      </div>
      <div class="detail-card">
        <p style="color:var(--text-dim);margin-bottom:14px;font-size:13px;">
          💡 ₹10 fee deducted only after successful submission.
        </p>
        <div class="field">
          <label>Service Name</label>
          <input type="text" id="svName" placeholder="2-60 chars"/>
        </div>
        <div class="field">
          <label>Price (INR)</label>
          <input type="number" id="svPrice" placeholder="e.g. 100"/>
        </div>
        <div class="field">
          <label>Your Telegram Username</label>
          <input type="text" id="svContact" placeholder="e.g. @yourname"/>
        </div>
        <div class="field">
          <label>Description</label>
          <input type="text" id="svDesc" placeholder="10-400 chars description"/>
        </div>
        <button class="btn btn-green" style="width:100%;" onclick="submitService()">✅ Submit Service</button>
      </div>
    </div>

    <!-- ============ OWNER PANEL ============ -->
    <div class="page" id="page-owner">
      <div class="page-head">
        <div class="back-btn" onclick="goto('home')">←</div>
        <h2>👑 Owner Panel</h2>
      </div>

      <div class="stat-grid">
        <div class="stat"><div class="lbl">Total Users</div><div class="val" id="stUsers">0</div></div>
        <div class="stat"><div class="lbl">Total Balance</div><div class="val" id="stBal">₹0</div></div>
        <div class="stat"><div class="lbl">Countries</div><div class="val" id="stCountries">0</div></div>
        <div class="stat"><div class="lbl">Pending Pays</div><div class="val" id="stPending">0</div></div>
      </div>

      <div class="owner-grid">
        <div class="menu-card owner" onclick="goto('ownAdd')"><div class="menu-icon">➕</div><h3>Add Numbers</h3></div>
        <div class="menu-card owner" onclick="goto('ownDel')"><div class="menu-icon">🗑</div><h3>Delete Country</h3></div>
        <div class="menu-card owner" onclick="goto('ownPay')"><div class="menu-icon">💳</div><h3>Pending Pays</h3></div>
        <div class="menu-card owner" onclick="goto('ownDisc')"><div class="menu-icon">🏷</div><h3>Create Discount</h3></div>
        <div class="menu-card owner" onclick="goto('ownCpn')"><div class="menu-icon">🎟</div><h3>Create Coupon</h3></div>
        <div class="menu-card owner" onclick="goto('ownBC')"><div class="menu-icon">📣</div><h3>Broadcast</h3></div>
        <div class="menu-card owner" onclick="goto('ownUB')"><div class="menu-icon">💰</div><h3>User Balances</h3></div>
        <div class="menu-card owner" onclick="goto('ownBalMgr')"><div class="menu-icon">⚖️</div><h3>Add / Deduct Balance</h3></div>
      </div>
    </div>

    <!-- OWNER ADD NUMBERS -->
    <div class="page" id="page-ownAdd">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>➕ Add Country / Stock</h2>
      </div>
      <div class="detail-card">
        <div class="field"><label>Country Name</label><input type="text" id="oCountry" placeholder="e.g. USA"/></div>
        <div class="field"><label>Price per Account (INR)</label><input type="number" id="oPrice" placeholder="e.g. 60"/></div>
        <div class="field"><label>Quantity to Add</label><input type="number" id="oQty" placeholder="e.g. 10"/></div>
        <button class="btn btn-green" style="width:100%;" onclick="ownerAddCountry()">✅ Add to Stock</button>
      </div>
    </div>

    <!-- OWNER DELETE -->
    <div class="page" id="page-ownDel">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>🗑 Delete Country</h2>
      </div>
      <div id="delList"></div>
    </div>

    <!-- PENDING PAYMENTS -->
    <div class="page" id="page-ownPay">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>💳 Pending Payments</h2>
      </div>
      <div id="payList"></div>
    </div>

    <!-- DISCOUNT -->
    <div class="page" id="page-ownDisc">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>🏷 Create Discount Code</h2>
      </div>
      <div class="detail-card">
        <div class="field"><label>Discount Amount (INR)</label><input type="number" id="oDisc" placeholder="e.g. 10"/></div>
        <button class="btn btn-neon" style="width:100%;" onclick="ownerCreateDisc()">🎟 Generate Code</button>
        <div id="discResult" style="margin-top:14px;"></div>
      </div>
      <div style="margin-top:20px;" id="discList"></div>
    </div>

    <!-- COUPON OWNER -->
    <div class="page" id="page-ownCpn">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>🎟 Create Coupon</h2>
      </div>
      <div class="detail-card">
        <div class="field"><label>Coupon Amount (INR)</label><input type="number" id="oCpn" placeholder="e.g. 50"/></div>
        <button class="btn btn-gold" style="width:100%;" onclick="ownerCreateCpn()">🎁 Generate Coupon</button>
        <div id="cpnResult" style="margin-top:14px;"></div>
      </div>
      <div style="margin-top:20px;" id="cpnList"></div>
    </div>

    <!-- BROADCAST -->
    <div class="page" id="page-ownBC">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>📣 Broadcast</h2>
      </div>
      <div class="detail-card">
        <div class="field"><label>Message</label><input type="text" id="bcMsg" placeholder="Type your broadcast..."/></div>
        <button class="btn btn-neon" style="width:100%;" onclick="ownerBroadcast()">📤 Send to All Users</button>
        <div id="bcMessages" style="margin-top:20px;"></div>
      </div>
    </div>

    <!-- USER BALANCES -->
    <div class="page" id="page-ownUB">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>💰 User Balances</h2>
      </div>
      <div id="ubList"></div>
    </div>

    <!-- BALANCE MANAGER -->
    <div class="page" id="page-ownBalMgr">
      <div class="page-head">
        <div class="back-btn" onclick="goto('owner')">←</div>
        <h2>⚖️ Add / Deduct Balance</h2>
      </div>
      <div class="detail-card">
        <div class="field"><label>Username</label><input type="text" id="bmUser" placeholder="Target username"/></div>
        <div class="field"><label>Amount (INR)</label><input type="number" id="bmAmt" placeholder="Amount"/></div>
        <div class="actions">
          <button class="btn btn-green" onclick="ownerBalAction('add')">➕ Add</button>
          <button class="btn btn-red" onclick="ownerBalAction('deduct')">➖ Deduct</button>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- ============ MODAL: OWNER PASSWORD ============ -->
<div class="modal-bg" id="ownerModal">
  <div class="modal">
    <h3>👑 Owner Access</h3>
    <p style="color:var(--text-dim);font-size:13px;margin-bottom:14px;">Enter owner password to access admin panel.</p>
    <div class="field">
      <label>Password</label>
      <input type="password" id="ownerPass" placeholder="Owner password"/>
    </div>
    <div class="actions">
      <button class="btn btn-ghost" onclick="closeOwnerModal()">Cancel</button>
      <button class="btn btn-gold" onclick="verifyOwnerPass()">🔓 Unlock</button>
    </div>
  </div>
</div>

<!-- ============ MODAL: BUY ACCOUNT ============ -->
<div class="modal-bg" id="buyModal">
  <div class="modal">
    <h3>🛒 Buy Accounts</h3>
    <div id="buyModalBody"></div>
    <div class="field">
      <label>Quantity</label>
      <input type="number" id="buyQty" min="1" placeholder="How many?"/>
    </div>
    <div class="actions">
      <button class="btn btn-ghost" onclick="closeBuy()">Cancel</button>
      <button class="btn btn-green" onclick="confirmBuy()">✅ Confirm Purchase</button>
    </div>
  </div>
</div>

<script>
/* =============================================================
   ZUDOOTP WEBSITE - Pure Client-Side (LocalStorage)
   Auto-approve deposit, full owner panel, marketplace, etc.
   ============================================================= */

const OWNER_PASS = "ZUDOOTPZUDO";
const DB_KEY = "zudootp_db_v1";
const SESSION_KEY = "zudootp_session";
const SERVICE_FEE = 10;
const MIN_DEPOSIT = 1;

const FLAGS = {USA:"🇺🇸",UK:"🇬🇧",INDIA:"🇮🇳",CANADA:"🇨🇦",AUSTRALIA:"🇦🇺",GERMANY:"🇩🇪",FRANCE:"🇫🇷",KENYA:"🇰🇪",NIGERIA:"🇳🇬",PAKISTAN:"🇵🇰",JAPAN:"🇯🇵",CHINA:"🇨🇳",BRAZIL:"🇧🇷",RUSSIA:"🇷🇺",SPAIN:"🇪🇸"};

/* ---------- DB Helpers ---------- */
function loadDB(){
  let raw = localStorage.getItem(DB_KEY);
  if(!raw){
    const fresh = {
      users:{},
      accounts:{
        "USA":{price:60,quantity:5},
        "INDIA":{price:30,quantity:10},
        "UK":{price:80,quantity:3}
      },
      discounts:{},
      coupons:{},
      services:{},
      service_seq:0,
      pending:[],
      broadcasts:[],
      used_utrs:{}
    };
    localStorage.setItem(DB_KEY,JSON.stringify(fresh));
    return fresh;
  }
  try{return JSON.parse(raw);}catch(e){return {};}
}
function saveDB(){localStorage.setItem(DB_KEY,JSON.stringify(db));}
let db = loadDB();
let session = JSON.parse(localStorage.getItem(SESSION_KEY) || "null");
let currentCountry = null;
let isOwnerUnlocked = false;

/* ---------- UI Helpers ---------- */
function toast(msg,type="ok"){
  const w=document.getElementById("toastWrap");
  const t=document.createElement("div");
  t.className="toast "+type;
  t.innerHTML=msg;
  w.appendChild(t);
  setTimeout(()=>{t.style.opacity=0;t.style.transform="translateX(120%)";},3000);
  setTimeout(()=>t.remove(),3400);
}
function escapeHTML(s){return String(s||"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}

/* ---------- Particles ---------- */
function spawnParticles(){
  const c=document.getElementById("particles");
  for(let i=0;i<25;i++){
    const p=document.createElement("div");
    p.className="particle";
    const sz=Math.random()*6+3;
    p.style.width=sz+"px";p.style.height=sz+"px";
    p.style.left=Math.random()*100+"%";
    p.style.animationDuration=(Math.random()*15+8)+"s";
    p.style.animationDelay=Math.random()*8+"s";
    c.appendChild(p);
  }
}
spawnParticles();

/* ============ AUTH ============ */
function switchTab(t){
  document.getElementById("tabLogin").classList.toggle("active",t==="login");
  document.getElementById("tabReg").classList.toggle("active",t==="reg");
  document.getElementById("loginForm").style.display=t==="login"?"":"none";
  document.getElementById("regForm").style.display=t==="reg"?"":"none";
  document.getElementById("authMsg").className="auth-msg";
}
function showAuthMsg(msg,ok=false){
  const e=document.getElementById("authMsg");
  e.textContent=msg;
  e.className="auth-msg "+(ok?"ok":"error");
}
function doRegister(){
  const u=document.getElementById("regUser").value.trim();
  const p=document.getElementById("regPass").value;
  const p2=document.getElementById("regPass2").value;
  if(!u||u.length<3) return showAuthMsg("❌ Username must be 3+ chars");
  if(!/^[a-zA-Z0-9_]+$/.test(u)) return showAuthMsg("❌ Only letters, numbers, underscore");
  if(p.length<4) return showAuthMsg("❌ Password min 4 chars");
  if(p!==p2) return showAuthMsg("❌ Passwords don't match");
  if(db.users[u]) return showAuthMsg("❌ Username already taken");
  db.users[u]={password:p,balance:0,purchases:[],created:new Date().toISOString(),usedDiscounts:[]};
  saveDB();
  showAuthMsg("✅ Account created! Logging in...",true);
  setTimeout(()=>{
    session={username:u};
    localStorage.setItem(SESSION_KEY,JSON.stringify(session));
    enterApp();
  },800);
}
function doLogin(){
  const u=document.getElementById("loginUser").value.trim();
  const p=document.getElementById("loginPass").value;
  if(!u||!p) return showAuthMsg("❌ Fill all fields");
  const user=db.users[u];
  if(!user) return showAuthMsg("❌ User not found. Please register.");
  if(user.password!==p) return showAuthMsg("❌ Wrong password");
  session={username:u};
  localStorage.setItem(SESSION_KEY,JSON.stringify(session));
  showAuthMsg("✅ Login successful!",true);
  setTimeout(enterApp,500);
}
function doLogout(){
  localStorage.removeItem(SESSION_KEY);
  session=null;isOwnerUnlocked=false;
  document.getElementById("app").classList.remove("show");
  document.getElementById("authScreen").style.display="flex";
  toast("👋 Logged out","ok");
}
function enterApp(){
  document.getElementById("authScreen").style.display="none";
  document.getElementById("app").classList.add("show");
  refreshUI();
  goto("home");
}

/* ============ NAVIGATION ============ */
function goto(p){
  document.querySelectorAll(".page").forEach(x=>x.classList.remove("active"));
  const el=document.getElementById("page-"+p);
  if(el){el.classList.add("active");window.scrollTo(0,0);}
  if(p==="accounts") renderCountries();
  if(p==="profile") renderProfile();
  if(p==="history") renderHistory();
  if(p==="srvList") renderServices();
  if(p==="owner") renderOwner();
  if(p==="ownDel") renderDelList();
  if(p==="ownPay") renderPayList();
  if(p==="ownUB") renderUBList();
  if(p==="ownDisc") renderDiscList();
  if(p==="ownCpn") renderCpnList();
  if(p==="ownBC") renderBC();
}

/* ============ REFRESH UI ============ */
function refreshUI(){
  if(!session) return;
  const u=db.users[session.username];
  if(!u){doLogout();return;}
  document.getElementById("heroUser").textContent=session.username;
  document.getElementById("walletBig").textContent="💎 ₹"+u.balance.toFixed(2);
  document.getElementById("balancePill").textContent="💎 ₹"+u.balance.toFixed(2);
}

/* ============ COUNTRIES ============ */
function renderCountries(){
  const list=document.getElementById("countryList");
  const keys=Object.keys(db.accounts).filter(k=>db.accounts[k].quantity>0);
  if(!keys.length){
    list.innerHTML='<div class="empty"><div class="ic">📭</div><h3>No accounts available</h3><p>Check back soon!</p></div>';
    return;
  }
  list.innerHTML=keys.map(c=>{
    const a=db.accounts[c];const f=FLAGS[c.toUpperCase()]||"📱";
    return `<div class="country-card" onclick="openCountry('${c}')">
      <div class="country-flag">${f}</div>
      <h4>${escapeHTML(c)}</h4>
      <div class="country-meta">
        <span class="stock">📦 ${a.quantity} in stock</span>
        <span class="price">₹${a.price}</span>
      </div>
    </div>`;
  }).join("");
}
function openCountry(c){
  currentCountry=c;
  const a=db.accounts[c];const u=db.users[session.username];
  document.getElementById("cdTitle").innerHTML=(FLAGS[c.toUpperCase()]||"📱")+" "+escapeHTML(c);
  document.getElementById("cdBody").innerHTML=`
    <h3>${escapeHTML(c)} Virtual Account</h3>
    <div class="detail-row"><span>💰 Price per account</span><span>₹${a.price}</span></div>
    <div class="detail-row"><span>📦 Available stock</span><span>${a.quantity}</span></div>
    <div class="detail-row"><span>💳 Your balance</span><span>₹${u.balance.toFixed(2)}</span></div>
    <p style="margin-top:14px;color:var(--text-dim);font-size:13px;">✨ 100% Working Sessions • ⚡ Instant OTP Delivery • 🔒 Secure</p>
    <div class="actions">
      <button class="btn btn-green" onclick="openBuy('${c}')">🛒 Buy Now</button>
      <button class="btn btn-gold" onclick="openDiscountModal()">🎟 Apply Discount</button>
    </div>`;
  goto("country");
}

/* ============ BUY MODAL ============ */
function openBuy(c){
  currentCountry=c;
  const a=db.accounts[c];
  document.getElementById("buyModalBody").innerHTML=`
    <p style="margin-bottom:10px;">Country: <b>${escapeHTML(c)}</b></p>
    <p style="margin-bottom:6px;">Price: <b>₹${a.price}/account</b></p>
    <p style="margin-bottom:14px;color:var(--text-dim);font-size:13px;">Available: ${a.quantity}</p>`;
  document.getElementById("buyQty").value="1";
  document.getElementById("buyQty").max=a.quantity;
  document.getElementById("buyModal").classList.add("show");
}
function closeBuy(){document.getElementById("buyModal").classList.remove("show");}
function confirmBuy(){
  const qty=parseInt(document.getElementById("buyQty").value);
  const a=db.accounts[currentCountry];const u=db.users[session.username];
  if(!qty||qty<1) return toast("❌ Invalid quantity","err");
  if(qty>a.quantity) return toast("❌ Only "+a.quantity+" available","err");
  const total=qty*a.price;
  if(u.balance<total) return toast("❌ Need ₹"+total+", have ₹"+u.balance,"err");
  u.balance-=total;a.quantity-=qty;
  const phones=[];
  for(let i=0;i<qty;i++){
    phones.push("+"+Math.floor(Math.random()*900+100)+Math.floor(Math.random()*9000000+1000000));
  }
  u.purchases.push({country:currentCountry,quantity:qty,price:total,phones:phones,date:new Date().toISOString()});
  saveDB();refreshUI();closeBuy();
  toast(`✅ Bought ${qty}x ${currentCountry}!<br>Phones: ${phones.join(", ")}`,"ok");
  setTimeout(()=>goto("history"),1000);
}

/* ============ DISCOUNT MODAL (inline using prompt) ============ */
function openDiscountModal(){
  const code=prompt("Enter discount code:");
  if(!code) return;
  const c=code.trim().toUpperCase();
  if(!db.discounts[c]) return toast("❌ Invalid code","err");
  const u=db.users[session.username];
  if(!u.usedDiscounts) u.usedDiscounts=[];
  if(u.usedDiscounts.includes(c)) return toast("❌ Already used by you","err");
  u.usedDiscounts.push(c);
  u.balance+=db.discounts[c].amount;
  saveDB();refreshUI();
  toast(`✅ Discount ₹${db.discounts[c].amount} applied!`,"ok");
}

/* ============ PROFILE ============ */
function renderProfile(){
  const u=db.users[session.username];
  document.getElementById("profileBody").innerHTML=`
    <h3>👤 ${escapeHTML(session.username)}</h3>
    <div class="detail-row"><span>💎 Balance</span><span>₹${u.balance.toFixed(2)}</span></div>
    <div class="detail-row"><span>📦 Total Purchases</span><span>${u.purchases.length}</span></div>
    <div class="detail-row"><span>💸 Total Spent</span><span>₹${u.purchases.reduce((s,p)=>s+p.price,0).toFixed(2)}</span></div>
    <div class="detail-row"><span>📅 Joined</span><span>${new Date(u.created).toLocaleDateString()}</span></div>
    <div class="actions"><button class="btn btn-neon" onclick="goto('deposit')">💰 Add Funds</button></div>`;
}

/* ============ HISTORY ============ */
function renderHistory(){
  const u=db.users[session.username];
  const body=document.getElementById("historyBody");
  if(!u.purchases.length){
    body.innerHTML='<div class="empty"><div class="ic">📭</div><h3>No history yet</h3><p>Start shopping!</p></div>';
    return;
  }
  body.innerHTML=u.purchases.slice().reverse().map(p=>`
    <div class="history-card">
      <div class="top">
        <b>${(FLAGS[p.country.toUpperCase()]||"📱")} ${escapeHTML(p.country)} × ${p.quantity}</b>
        <span class="amt">₹${p.price}</span>
      </div>
      <small style="color:var(--text-dim);">📞 ${(p.phones||[]).join(", ")||"—"}</small><br>
      <small style="color:var(--text-dim);">📅 ${new Date(p.date).toLocaleString()}</small>
    </div>`).join("");
}

/* ============ DEPOSIT - UPI QR ============ */
function genQR(){
  const amt=parseInt(document.getElementById("depAmount").value);
  if(!amt||amt<MIN_DEPOSIT) return toast("❌ Min ₹"+MIN_DEPOSIT,"err");
  const upi=`upi://pay?pa=fearlessaditya@fam&pn=Aditya&am=${amt}&cu=INR&tn=ZUDOOTPPay`;
  const qrUrl=`https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=${encodeURIComponent(upi)}`;
  document.getElementById("qrImg").src=qrUrl;
  document.getElementById("qrZone").style.display="block";
}
function submitDeposit(){
  const amt=parseInt(document.getElementById("depAmount").value);
  const utr=document.getElementById("depUTR").value.trim();
  if(!amt||amt<MIN_DEPOSIT) return toast("❌ Invalid amount","err");
  if(!utr||utr.length<6) return toast("❌ Enter valid UTR/Txn ID","err");
  if(db.used_utrs[utr.toUpperCase()]) return toast("❌ UTR already used","err");

  // Show loading
  toast("🤖 Auto-verifying payment...","warn");

  // Auto-approve simulation: if amount >= 1 and not used, approve after 2s
  setTimeout(()=>{
    db.used_utrs[utr.toUpperCase()]={user:session.username,amount:amt,at:new Date().toISOString()};
    const u=db.users[session.username];
    u.balance+=amt;
    saveDB();refreshUI();
    document.getElementById("depAmount").value="";
    document.getElementById("depUTR").value="";
    document.getElementById("qrZone").style.display="none";
    toast(`✅ Auto-Approved! ₹${amt} added`,"ok");
    setTimeout(()=>goto("home"),800);
  },2000);
}

/* ============ COUPON ============ */
function redeemCoupon(){
  const code=document.getElementById("couponInput").value.trim().toUpperCase();
  if(!code) return toast("❌ Enter code","err");
  const c=db.coupons[code];
  if(!c) return toast("❌ Invalid coupon","err");
  if(c.used) return toast("❌ Already used","err");
  c.used=true;c.usedBy=session.username;c.usedAt=new Date().toISOString();
  const u=db.users[session.username];u.balance+=c.amount;
  saveDB();refreshUI();
  document.getElementById("couponInput").value="";
  toast(`✅ Redeemed ₹${c.amount}!`,"ok");
  setTimeout(()=>goto("home"),800);
}

/* ============ SERVER 2 ============ */
function renderServices(){
  const body=document.getElementById("srvListBody");
  const arr=Object.values(db.services).filter(s=>s.active);
  if(!arr.length){
    body.innerHTML='<div class="empty"><div class="ic">📭</div><h3>No services yet</h3></div>';
    return;
  }
  body.innerHTML=arr.map(s=>`
    <div class="list-item">
      <div class="info">
        <b>🛍 ${escapeHTML(s.name)}</b>
        <small>👤 @${escapeHTML(s.contact)} • ${escapeHTML(s.description.substring(0,80))}</small>
      </div>
      <div style="text-align:right;">
        <div style="color:var(--gold);font-weight:700;">₹${s.price}</div>
        <button class="btn btn-neon" style="margin-top:6px;padding:6px 12px;font-size:12px;" onclick="buyService('${s.id}')">Buy</button>
      </div>
    </div>`).join("");
}
function buyService(sid){
  const s=db.services[sid];if(!s) return;
  toast(`✅ Request sent! Contact @${s.contact} on Telegram`,"ok");
}
function submitService(){
  const name=document.getElementById("svName").value.trim();
  const price=parseInt(document.getElementById("svPrice").value);
  const contact=document.getElementById("svContact").value.trim().replace("@","");
  const desc=document.getElementById("svDesc").value.trim();
  if(!name||name.length<2||name.length>60) return toast("❌ Name 2-60 chars","err");
  if(!price||price<1) return toast("❌ Invalid price","err");
  if(!contact||contact.length<3) return toast("❌ Invalid contact","err");
  if(!desc||desc.length<10||desc.length>400) return toast("❌ Desc 10-400 chars","err");
  const u=db.users[session.username];
  if(u.balance<SERVICE_FEE) return toast(`❌ Need ₹${SERVICE_FEE} fee. Balance: ₹${u.balance}`,"err");
  u.balance-=SERVICE_FEE;
  db.service_seq=(db.service_seq||0)+1;
  const id="S"+db.service_seq;
  db.services[id]={id,name,price,contact,description:desc,owner:session.username,active:true,created:new Date().toISOString()};
  saveDB();refreshUI();
  document.getElementById("svName").value="";document.getElementById("svPrice").value="";
  document.getElementById("svContact").value="";document.getElementById("svDesc").value="";
  toast(`✅ Service added! ₹${SERVICE_FEE} fee deducted`,"ok");
  setTimeout(()=>goto("srvList"),800);
}

/* ============ OWNER PANEL ============ */
function openOwnerPanel(){
  if(isOwnerUnlocked){goto("owner");return;}
  document.getElementById("ownerPass").value="";
  document.getElementById("ownerModal").classList.add("show");
}
function closeOwnerModal(){document.getElementById("ownerModal").classList.remove("show");}
function verifyOwnerPass(){
  const p=document.getElementById("ownerPass").value;
  if(p===OWNER_PASS){
    isOwnerUnlocked=true;
    closeOwnerModal();
    toast("👑 Owner unlocked!","ok");
    goto("owner");
  } else {
    toast("❌ Wrong password!","err");
  }
}
function renderOwner(){
  if(!isOwnerUnlocked){goto("home");return;}
  document.getElementById("stUsers").textContent=Object.keys(db.users).length;
  const totalBal=Object.values(db.users).reduce((s,u)=>s+u.balance,0);
  document.getElementById("stBal").textContent="₹"+totalBal.toFixed(0);
  document.getElementById("stCountries").textContent=Object.keys(db.accounts).length;
  document.getElementById("stPending").textContent=(db.pending||[]).filter(p=>p.status==="pending").length;
}
function ownerAddCountry(){
  if(!isOwnerUnlocked) return;
  const c=document.getElementById("oCountry").value.trim().toUpperCase();
  const p=parseInt(document.getElementById("oPrice").value);
  const q=parseInt(document.getElementById("oQty").value);
  if(!c) return toast("❌ Enter country","err");
  if(!p||p<1) return toast("❌ Invalid price","err");
  if(!q||q<1) return toast("❌ Invalid qty","err");
  if(!db.accounts[c]) db.accounts[c]={price:p,quantity:0};
  db.accounts[c].price=p;db.accounts[c].quantity+=q;
  saveDB();
  document.getElementById("oCountry").value="";document.getElementById("oPrice").value="";document.getElementById("oQty").value="";
  toast(`✅ Added ${q}x ${c} @ ₹${p}`,"ok");
}
function renderDelList(){
  const body=document.getElementById("delList");
  const keys=Object.keys(db.accounts);
  if(!keys.length){body.innerHTML='<div class="empty"><div class="ic">📭</div><h3>No countries</h3></div>';return;}
  body.innerHTML=keys.map(c=>`
    <div class="list-item">
      <div class="info">
        <b>${(FLAGS[c]||"📱")} ${escapeHTML(c)}</b>
        <small>Stock: ${db.accounts[c].quantity} • ₹${db.accounts[c].price}</small>
      </div>
      <button class="btn btn-red" onclick="delCountry('${c}')">🗑 Delete</button>
    </div>`).join("");
}
function delCountry(c){
  if(!confirm("Delete "+c+"?")) return;
  delete db.accounts[c];saveDB();renderDelList();
  toast(`✅ Deleted ${c}`,"ok");
}
function renderPayList(){
  const body=document.getElementById("payList");
  const pending=(db.pending||[]).filter(p=>p.status==="pending");
  if(!pending.length){body.innerHTML='<div class="empty"><div class="ic">✅</div><h3>No pending</h3></div>';return;}
  body.innerHTML=pending.map((p,i)=>`
    <div class="list-item">
      <div class="info"><b>${escapeHTML(p.user)}</b><small>₹${p.amount} • UTR: ${escapeHTML(p.utr)}</small></div>
      <div style="display:flex;gap:6px;">
        <button class="btn btn-green" onclick="approvePay(${i})">✅</button>
        <button class="btn btn-red" onclick="rejectPay(${i})">❌</button>
      </div>
    </div>`).join("");
}
function approvePay(i){
  const pending=(db.pending||[]).filter(p=>p.status==="pending");
  const p=pending[i];if(!p) return;
  p.status="approved";
  if(db.users[p.user]) db.users[p.user].balance+=p.amount;
  saveDB();renderPayList();refreshUI();
  toast(`✅ Approved ${p.user} ₹${p.amount}`,"ok");
}
function rejectPay(i){
  const pending=(db.pending||[]).filter(p=>p.status==="pending");
  const p=pending[i];if(!p) return;
  p.status="rejected";saveDB();renderPayList();
  toast("❌ Rejected","warn");
}
function renderUBList(){
  const body=document.getElementById("ubList");
  const arr=Object.entries(db.users).filter(([u,d])=>d.balance>=1).sort((a,b)=>b[1].balance-a[1].balance);
  if(!arr.length){body.innerHTML='<div class="empty"><div class="ic">📭</div><h3>No users</h3></div>';return;}
  body.innerHTML=arr.map(([u,d])=>`
    <div class="list-item">
      <div class="info"><b>${escapeHTML(u)}</b><small>Joined ${new Date(d.created).toLocaleDateString()}</small></div>
      <div style="color:var(--gold);font-weight:700;">₹${d.balance.toFixed(2)}</div>
    </div>`).join("");
}
function ownerCreateDisc(){
  const a=parseInt(document.getElementById("oDisc").value);
  if(!a||a<1) return toast("❌ Invalid amount","err");
  const code="DSC"+Math.random().toString(36).substring(2,10).toUpperCase();
  db.discounts[code]={amount:a,created:new Date().toISOString()};
  saveDB();
  document.getElementById("oDisc").value="";
  document.getElementById("discResult").innerHTML=`
    <div class="list-item" style="background:rgba(0,255,136,0.1);border-color:var(--green);">
      <div class="info"><b>🎟 ${code}</b><small>₹${a} discount</small></div>
      <button class="btn btn-ghost" onclick="navigator.clipboard.writeText('${code}');toast('📋 Copied!','ok')">📋</button>
    </div>`;
  renderDiscList();
  toast("✅ Code generated!","ok");
}
function renderDiscList(){
  const body=document.getElementById("discList");
  const arr=Object.entries(db.discounts);
  if(!arr.length){body.innerHTML="";return;}
  body.innerHTML="<h4 style='margin-bottom:10px;'>📋 All Discount Codes</h4>"+arr.map(([code,d])=>`
    <div class="list-item">
      <div class="info"><b>${code}</b><small>₹${d.amount}</small></div>
      <button class="btn btn-red" onclick="delDisc('${code}')">🗑</button>
    </div>`).join("");
}
function delDisc(c){delete db.discounts[c];saveDB();renderDiscList();toast("✅ Deleted","ok");}

function ownerCreateCpn(){
  const a=parseInt(document.getElementById("oCpn").value);
  if(!a||a<1) return toast("❌ Invalid amount","err");
  const code="CPN"+Math.random().toString(36).substring(2,12).toUpperCase();
  db.coupons[code]={amount:a,used:false,created:new Date().toISOString()};
  saveDB();
  document.getElementById("oCpn").value="";
  document.getElementById("cpnResult").innerHTML=`
    <div class="list-item" style="background:rgba(255,215,0,0.1);border-color:var(--gold);">
      <div class="info"><b>🎁 ${code}</b><small>₹${a} • One-time use</small></div>
      <button class="btn btn-ghost" onclick="navigator.clipboard.writeText('${code}');toast('📋 Copied!','ok')">📋</button>
    </div>`;
  renderCpnList();
  toast("✅ Coupon created!","ok");
}
function renderCpnList(){
  const body=document.getElementById("cpnList");
  const arr=Object.entries(db.coupons);
  if(!arr.length){body.innerHTML="";return;}
  body.innerHTML="<h4 style='margin-bottom:10px;'>📋 All Coupons</h4>"+arr.map(([code,d])=>`
    <div class="list-item">
      <div class="info"><b>${code}</b><small>₹${d.amount} • ${d.used?"❌ Used by "+d.usedBy:"✅ Available"}</small></div>
      <button class="btn btn-red" onclick="delCpn('${code}')">🗑</button>
    </div>`).join("");
}
function delCpn(c){delete db.coupons[c];saveDB();renderCpnList();toast("✅ Deleted","ok");}

function ownerBroadcast(){
  const m=document.getElementById("bcMsg").value.trim();
  if(!m) return toast("❌ Enter message","err");
  db.broadcasts=db.broadcasts||[];
  db.broadcasts.push({msg:m,from:session.username,at:new Date().toISOString()});
  saveDB();
  document.getElementById("bcMsg").value="";
  toast(`📣 Broadcast sent to ${Object.keys(db.users).length} users`,"ok");
  renderBC();
}
function renderBC(){
  const body=document.getElementById("bcMessages");
  const arr=(db.broadcasts||[]).slice().reverse();
  if(!arr.length){body.innerHTML="";return;}
  body.innerHTML="<h4 style='margin-bottom:10px;'>📋 Recent Broadcasts</h4>"+arr.slice(0,10).map(b=>`
    <div class="history-card">
      <div class="top"><b>📣 Broadcast</b><span style="font-size:12px;color:var(--text-dim);">${new Date(b.at).toLocaleString()}</span></div>
      <div style="margin-top:4px;">${escapeHTML(b.msg)}</div>
    </div>`).join("");
}

function ownerBalAction(act){
  const u=document.getElementById("bmUser").value.trim();
  const a=parseInt(document.getElementById("bmAmt").value);
  if(!db.users[u]) return toast("❌ User not found","err");
  if(!a||a<1) return toast("❌ Invalid amount","err");
  if(act==="add"){db.users[u].balance+=a;toast(`➕ ₹${a} added to ${u}`,"ok");}
  else{
    if(db.users[u].balance<a) return toast("❌ User has only ₹"+db.users[u].balance,"err");
    db.users[u].balance-=a;toast(`➖ ₹${a} deducted from ${u}`,"ok");
  }
  saveDB();refreshUI();
  document.getElementById("bmUser").value="";document.getElementById("bmAmt").value="";
}

/* ============ INIT ============ */
if(session && db.users[session.username]){
  enterApp();
} else {
  document.getElementById("authScreen").style.display="flex";
}

// Enter key support
document.addEventListener("keydown",e=>{
  if(e.key==="Enter"){
    if(document.getElementById("loginForm").offsetParent && document.getElementById("loginForm").style.display!=="none")
      doLogin();
    else if(document.getElementById("regForm").offsetParent && document.getElementById("regForm").style.display!=="none")
      doRegister();
    else if(document.getElementById("ownerModal").classList.contains("show"))
      verifyOwnerPass();
  }
});
</script>
</body>
</html>
