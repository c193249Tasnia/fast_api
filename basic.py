<!DOCTYPE html>
<!-- saved from url=(0097)https://github.com/NTNirjana/session-2-%2Dfastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c -->
<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark" data-a11y-animated-images="system" data-a11y-link-underlines="true" data-turbo-loaded=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><style type="text/css">.turbo-progress-bar {
  position: fixed;
  display: block;
  top: 0;
  left: 0;
  height: 3px;
  background: #0076ff;
  z-index: 2147483647;
  transition:
    width 300ms ease-out,
    opacity 150ms 150ms ease-in;
  transform: translate3d(0, 0, 0);
}
</style>
    
  
  
  
  
  
  

  

  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/light-3e154969b9f9.css"><link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/dark-9c5b7a476542.css"><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-afda8eb0fb33.css"><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-2494e44ccdc5.css"><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-56fff47acadc.css"><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-71cd4cc132ec.css"><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-fd5499848985.css"><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-31d17ba3e139.css"><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-68d6b2c79663.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/primer-primitives-fd4f6f126b06.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/primer-3f55af1462e6.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/global-561250c1bd8a.css">
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/github-e4eed26e112b.css">
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/repository-0f7cf89e325a.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/code-14def43eef8d.css">

  


  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["ab_test_homepage_what_is_copilot_video","code_vulnerability_scanning","copilot_beta_features_opt_in","copilot_chat_conversation_intent_knowledge_search_skill","copilot_chat_static_thread_suggestions","copilot_completion_new_domain","copilot_conversational_ux_history_refs","copilot_copy_message","copilot_followup_to_agent","copilot_implicit_context","copilot_smell_icebreaker_ux","custom_inp","experimentation_azure_variant_endpoint","failbot_handle_non_errors","filter_prefetch_suggestions","geojson_azure_maps","ghost_pilot_confidence_truncation_25","ghost_pilot_stream_handling","hovercard_accessibility","hovercard_longer_activate_timeout","marketing_pages_search_explore_provider","primer_react_css_modules_ga","remove_child_patch","repository_suggester_elastic_search","sample_network_conn_type","site_metered_billing_update"]}</script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/wp-runtime-9371de7510a4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_dompurify_dist_purify_js-89a69c248502.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_oddbird_popover-polyfill_dist_popover_js-56729c905fe2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_arianotify-polyfill_ariaNotify-polyfill_js-node_modules_github_mi-247092-627b030d3acc.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/environment-924e60bca7d2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_selector-observer_dist_index_esm_js-f690fd9ae3d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_behaviors_dist_esm_focus-zone_js-c9086a4fb62b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_relative-time-element_dist_index_js-7b95699705bc.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_behaviors_dist_esm_anchored-position_js-node_modules_fzy_js_index-192fd2-a07608c791cf.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_auto-complete-element_dist_index_js-node_modules_github_details-d-ed9a97-841122a1e9d4.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_text-expander-element_dist_index_js-cd48220d74d5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_delegated-events_dist_in-3efda3-701acb69193f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_filter-input-element_dist_index_js-node_modules_github_remote-inp-2e8678-34feeec9c894.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_clipboard-copy-element_-782ca5-54763cd55b96.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_primer_view-co-10eecb-8056ef83b81e.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/ui_packages_onfocus_onfocus_ts-ui_packages_trusted-types-policies_policy_ts-ui_packages_trust-0eb5c4-372296785620.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/github-elements-508a45ca23c6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/element-registry-4504b7d8c3d8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_catalyst_lib_index_js-node_modules_github_hydro-analytics-client_-7901e7-dc88587c14ed.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_braintree_browser-detection_dist_browser-detection_js-node_modules_stack-68835d-a18220f1db8d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_lit-html_lit-html_js-ce7225a304c5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_morphdom_dist_morphdom-e-7c534c-f8a5485c982a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_turbo_dist_turbo_es2017-esm_js-858e043fcf76.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-893f9f-6cf3320416b8.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_scroll-anchoring_dist_scroll-anchoring_esm_js-node_modules_github_hotkey-1a1d91-fa9f29a8514b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_color-convert_index_js-0e07cc183eed.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_session-resume_dist_index_js-node_modules_primer_behaviors_dist_e-ac74c6-5e03381c44b5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_behaviors_dist_esm_dimensions_js-node_modules_github_jtml_lib_index_js-53b423ede32a.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_quote-selection_dist_index_js-node_modules_github_textarea-autosi-9e0349-ab4976fc78a6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/ui_packages_updatable-content_updatable-content_ts-a2009221d154.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_behaviors_task-list_ts-app_assets_modules_github_sso_ts-ui_packages-e1ce06-30f9d5de7ad2.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_sticky-scroll-into-view_ts-112600808cf9.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_behaviors_ajax-error_ts-app_assets_modules_github_behaviors_include-467754-8979fbf79bf6.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_behaviors_commenting_edit_ts-app_assets_modules_github_behaviors_ht-83c235-aeae6fcdf371.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_blob-anchor_ts-app_assets_modules_github_jump-to_page-views_ts-ui_p-38f236-6918e89ea155.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/behaviors-b43b83716346.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_delegated-events_dist_index_js-node_modules_github_catalyst_lib_index_js-06ff531-bf7e5a3732fd.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/notifications-global-54f34167118d.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_virtualized-list_es_index_js-node_modules_github_template-parts_lib_index_js-96453a51f920.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-e53a3f-62113d33abd1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_ref-selector_ts-00df584d9e79.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/codespaces-005e47f4f276.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_file-attachment-element_dist_index_js-node_modules_github_filter--e7f8b0-c7aaf10ff072.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_repositories_get-repo-element_ts-78999cbaea69.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/repositories-57ecf4afba64.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_github_catalyst_lib_inde-dbbea9-e73b311a14f1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/code-menu-a8d08997ac4f.js.download"></script>
  
  <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/react-lib-7b7b5264f6c1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_primer_octicons-react_di-b40d97-2d816f3aa913.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-55a9038b54f0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-b0edbfb6a9e5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_TooltipV2_Tooltip_js-4d5019830e3c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_node_modules_primer_octicons-react_dist_index_esm_mjs-a5155473fc69.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-fd5a7039f225.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-node_modules_primer_react_-5b2420-50d72766db7f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Text_Text_js-node_modules_primer_react_lib-esm_Text-7845da-9371f5bac483.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_FormControl_FormControl_js-1f51ab2bdcca.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_FilteredActionList_FilteredActionList_js-5a52bf212e2b.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Dialog_js-node_modules_primer_react_lib-esm_Feature-cdf735-4b63b6308961.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/ui_packages_react-core_create-browser-history_ts-ui_packages_safe-storage_safe-storage_ts-ui_-682c2c-40bb20608465.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/notifications-subscriptions-menu-075bd700538b.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/primer-react-css.8570b2718b0a9c0c8387.module.css">
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/notifications-subscriptions-menu.1bcff9205c241e99cff2.module.css">


  



  
  
  

    
  


  


    


  
  

  
  

    



  

  




    

  

    

    

      

      

    
    
    

      
  
  


      
      


      


      
      

        


  <meta http-equiv="x-pjax-version" content="54e6eaabf290f5701ae0ac35fad12f79afbac12bd691f0bb9d4d7322106a903b" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="43bc2a0e2750a1219c17b5bf1ec22aae37041bbc018bc5e27bb7708f80e7ab88" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="fccf03f5b6a75b525f9275cba7313774f880dbf7bfc1c8feacff07fc90de9ca0" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="5d0811d5864010aca1860f1bef99dd6cd4bfb20b3f8db124cc509b79487b7ad0" data-turbo-track="reload">

  

      
  

  



      


    


  

  

  
  
  





  

  <style data-styled="active" data-styled-version="5.3.6"></style><style id="ms-consent-banner-main-styles">.w8hcgFksdo30C8w-bygqu{color:#000}.ydkKdaztSS0AeHWIeIHsQ a{color:#0067B8}.erL690_8JwUW-R4bJRcfl{background-color:#EBEBEB;border:none;color:#000}.erL690_8JwUW-R4bJRcfl:enabled:hover{color:#000;background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}.erL690_8JwUW-R4bJRcfl:enabled:focus{background-color:#DBDBDB;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}.erL690_8JwUW-R4bJRcfl:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2);border:none}._1zNQOqxpBFSokeCLGi_hGr{border:none;background-color:#0067B8;color:#fff}._1zNQOqxpBFSokeCLGi_hGr:enabled:hover{color:#fff;background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:none}._1zNQOqxpBFSokeCLGi_hGr:enabled:focus{background-color:#0067B8;box-shadow:0px 4px 10px rgba(0,0,0,0.25);border:2px solid #000}._1zNQOqxpBFSokeCLGi_hGr:disabled{opacity:1;color:rgba(0,0,0,0.2);background-color:rgba(0,120,215,0.2);border:none}._23tra1HsiiP6cT-Cka-ycB{position:relative;display:flex;z-index:9999;width:100%;background-color:#F2F2F2;justify-content:space-between;text-align:left}div[dir="rtl"]._23tra1HsiiP6cT-Cka-ycB{text-align:right}._1Upc2NjY8AlDn177YoVj0y{margin:0;padding-left:5%;padding-top:8px;padding-bottom:8px}div[dir="rtl"] ._1Upc2NjY8AlDn177YoVj0y{margin:0;padding:8px 5% 8px 0;float:none}._23tra1HsiiP6cT-Cka-ycB svg{fill:none;max-width:none;max-height:none}._1V_hlU-7jdtPiooHMu89BB{display:table-cell;padding:12px;width:24px;height:24px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:24px;line-height:0}.f6QKJD7fhSbnJLarTL-W-{display:table-cell;vertical-align:middle;padding:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:16px}.f6QKJD7fhSbnJLarTL-W- a{text-decoration:underline}._2j0fmugLb1FgYz6KPuB91w{display:inline-block;margin-left:5%;margin-right:5%;min-width:40%;min-width:calc((150px + 3 * 4px) * 2 + 150px);min-width:-webkit-fit-content;min-width:-moz-fit-content;min-width:fit-content;align-self:center;position:relative}._1XuCi2WhiqeWRUVp3pnFG3{margin:4px;padding:5px;min-width:150px;min-height:36px;vertical-align:top;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._1XuCi2WhiqeWRUVp3pnFG3:focus{box-sizing:border-box}._1XuCi2WhiqeWRUVp3pnFG3:disabled{cursor:not-allowed}._2bvsb3ubApyZ0UGoQA9O9T{display:block;position:fixed;z-index:10000;top:0;left:0;width:100%;height:100%;background-color:rgba(255,255,255,0.6);overflow:auto;text-align:left}div[dir="rtl"]._2bvsb3ubApyZ0UGoQA9O9T{text-align:right}div[dir="rtl"] ._2bvsb3ubApyZ0UGoQA9O9T{left:auto;right:0}.AFsJE948muYyzCMktdzuk{position:relative;top:8%;margin-bottom:40px;margin-left:auto;margin-right:auto;box-sizing:border-box;width:640px;background-color:#fff;border:1px solid #0067B8}._3kWyBRbW_dgnMiEyx06Fu4{float:right;z-index:1;margin:2px;padding:12px;border:none;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:13px;line-height:13px;display:flex;align-items:center;text-align:center;color:#666;background-color:#fff}div[dir="rtl"] ._3kWyBRbW_dgnMiEyx06Fu4{margin:2px;padding:12px;float:left}.uCYvKvHXrhjNgflv1VqdD{position:static;margin-top:36px;margin-left:36px;margin-right:36px}._17pX1m9O_W--iZbDt3Ta5r{margin-top:0;margin-bottom:12px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:20px;line-height:24px;text-transform:none}._1kBkHQ1V1wu3kl-YcLgUr6{height:446px;overflow:auto}._20_nXDf6uFs9Q6wxRXG-I-{margin-top:0;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._20_nXDf6uFs9Q6wxRXG-I- a{text-decoration:underline}dl._2a0NH_GDQEQe5Ynfo7suVH{margin-top:36px;margin-bottom:0;padding:0;list-style:none;text-transform:none}dt._3j_LCPv7fyXv3A8FIXVwZ4{margin-top:20px;float:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;list-style:none}.k-vxTGFbdq1aOZB2HHpjh{margin:0;padding:0;border:none}._2Bucyy75c_ogoU1g-liB5R{margin:0;padding:0;border-bottom:none;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:600;font-size:18px;line-height:24px;text-transform:none}._63gwfzV8dclrsl2cfd90r{display:inline-block;margin-top:0;margin-bottom:13px;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px}._1l8wM_4mRYGz3Iu7l3BZR7{display:block}._2UE03QS02aZGkslegN_F-i{display:inline-block;position:relative;left:5px;margin-bottom:13px;margin-right:34px;padding:3px}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{margin:0 0 13px 34px;padding:3px;float:none}div[dir="rtl"] ._2UE03QS02aZGkslegN_F-i{left:auto;right:5px}._23tra1HsiiP6cT-Cka-ycB *::before,._2bvsb3ubApyZ0UGoQA9O9T *::before,._23tra1HsiiP6cT-Cka-ycB *::after,._2bvsb3ubApyZ0UGoQA9O9T *::after{box-sizing:inherit}._1HSFn0HzGo6w4ADApV8-c4{outline:2px solid rgba(0,0,0,0.8)}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2{display:inline-block;position:relative;margin-top:0;margin-left:0;margin-right:0;height:0;width:0;border-radius:0;cursor:pointer;outline:none;box-sizing:border-box;-webkit-appearance:none;-moz-appearance:none;appearance:none}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{display:block;position:absolute;top:5px;left:3px;height:19px;width:19px;content:"";border-radius:50%;border:1px solid #000;background-color:#fff}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2+label::before{left:auto;right:3px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:rgba(0,0,0,0.8)}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:hover::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::before{border:1px solid #0067B8}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:not(:disabled)+label:focus::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{display:block;position:absolute;top:10px;left:8px;height:9px;width:9px;content:"";border-radius:50%;background-color:#000}div[dir="rtl"] input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked+label::after{left:auto;right:8px}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label{cursor:not-allowed}input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled+label::before{border:1px solid rgba(0,0,0,0.2);background-color:rgba(0,0,0,0.2)}._3RJzeL3l9Rl_lAQEm6VwdX{display:block;position:static;float:right;margin-top:0;margin-bottom:0;margin-left:19px;margin-right:0;padding-top:0;padding-bottom:0;padding-left:8px;padding-right:0;width:80%;width:calc(100% - 19px);font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-transform:none;cursor:pointer;box-sizing:border-box}div[dir="rtl"] ._3RJzeL3l9Rl_lAQEm6VwdX{margin:0 19px 0 0;padding:0 8px 0 0;float:left}.nohp3sIG12ZBhzcMnPala{margin-top:20px;margin-bottom:48px}._2uhaEsmeotZ3P-M0AXo2kF{padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._2uhaEsmeotZ3P-M0AXo2kF:focus{box-sizing:border-box}._2uhaEsmeotZ3P-M0AXo2kF:disabled{cursor:not-allowed}._3tOu1FJ59c_xz_PmI1lKV5{float:right;padding:0;width:278px;height:36px;cursor:pointer;font-family:Segoe UI, SegoeUI, Arial, sans-serif;font-style:normal;font-weight:normal;font-size:15px;line-height:20px;text-align:center}._3tOu1FJ59c_xz_PmI1lKV5:focus{box-sizing:border-box}._3tOu1FJ59c_xz_PmI1lKV5:disabled{cursor:not-allowed}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0;padding:0;float:left}@media only screen and (max-width: 768px){._2j0fmugLb1FgYz6KPuB91w,._1Upc2NjY8AlDn177YoVj0y{padding-top:8px;padding-bottom:12px;padding-left:3.75%;padding-right:3.75%;margin:0;width:92.5%}._23tra1HsiiP6cT-Cka-ycB{display:block}._1XuCi2WhiqeWRUVp3pnFG3{margin-bottom:8px;margin-left:0;margin-right:0;width:100%}._2bvsb3ubApyZ0UGoQA9O9T{overflow:hidden}.AFsJE948muYyzCMktdzuk{top:1.8%;width:93.33%;height:96.4%;overflow:hidden}.uCYvKvHXrhjNgflv1VqdD{margin-top:24px;margin-left:24px;margin-right:24px;height:100%}._1kBkHQ1V1wu3kl-YcLgUr6{height:62%;height:calc(100% - 188px);min-height:50%}._2uhaEsmeotZ3P-M0AXo2kF{width:100%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:12px;margin-left:0;width:100%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 12px 0;padding:0;float:none}}@media only screen and (max-width: 768px) and (orientation: landscape), only screen and (max-height: 260px), only screen and (max-width: 340px){.AFsJE948muYyzCMktdzuk{overflow:auto}}@media only screen and (max-height: 260px), only screen and (max-width: 340px){._1XuCi2WhiqeWRUVp3pnFG3{min-width:0}._3kWyBRbW_dgnMiEyx06Fu4{padding:3%}.uCYvKvHXrhjNgflv1VqdD{margin-top:3%;margin-left:3%;margin-right:3%}._17pX1m9O_W--iZbDt3Ta5r{margin-bottom:3%}._1kBkHQ1V1wu3kl-YcLgUr6{height:calc(79% - 64px)}.nohp3sIG12ZBhzcMnPala{margin-top:5%;margin-bottom:10%}._3tOu1FJ59c_xz_PmI1lKV5{margin-bottom:3%}div[dir="rtl"] ._3tOu1FJ59c_xz_PmI1lKV5{margin:0 0 3% 0;padding:0;float:none}}
</style><style type="text/css" id="ms-consent-banner-theme-styles">._23tra1HsiiP6cT-Cka-ycB {
            background-color: #24292f !important;
        }.w8hcgFksdo30C8w-bygqu {
            color: #ffffff !important;
        }.ydkKdaztSS0AeHWIeIHsQ a {
            color: #d8b9ff !important;
        }._2bvsb3ubApyZ0UGoQA9O9T {
            background-color: rgba(23, 23, 23, 0.8) !important;
        }.AFsJE948muYyzCMktdzuk {
            background-color: #24292f !important;
            border: 1px solid #d8b9ff !important;
        }._3kWyBRbW_dgnMiEyx06Fu4 {
            color: #d8b9ff !important;
            background-color: #24292f !important;
        }._1zNQOqxpBFSokeCLGi_hGr {
            border: 1px solid #ffffff !important;
            background-color: #ffffff !important;
            color: #1f2328 !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:hover {
            color: #1f2328 !important;
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 1px solid transparent !important;
        }._1zNQOqxpBFSokeCLGi_hGr:enabled:focus {
            background-color: #d8b9ff !important;
            box-shadow: none !important;
            border: 2px solid #ffffff !important;
        }._1zNQOqxpBFSokeCLGi_hGr:disabled {
            opacity: 0.5 !important;
            color: #1f2328 !important;
            background-color: #ffffff !important;
            border: 1px solid transparent !important;
        }.erL690_8JwUW-R4bJRcfl {
            border: 1px solid #eaeef2 !important;
            background-color: #32383f !important;
            color: #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:hover {
            color: #ffffff !important;
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 1px solid #ffffff !important;
        }.erL690_8JwUW-R4bJRcfl:enabled:focus {
            background-color: #24292f !important;
            box-shadow: none !important;
            border: 2px solid #6e7781 !important;
        }.erL690_8JwUW-R4bJRcfl:disabled {
            opacity: 0.5 !important;
            color: #ffffff !important;
            background-color: #424a53 !important;
            border: 1px solid #6e7781 !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label::before {
            border: 1px solid #d8b9ff !important;
            background-color: #24292f !important;
        }._1HSFn0HzGo6w4ADApV8-c4 {
            outline: 2px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:checked + label::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:hover::after {
            background-color: #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::before {
            border: 1px solid #ffffff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2 + label:focus::after {
            background-color: #d8b9ff !important;
        }input[type="radio"]._1dp8Vp5m3HwAqGx8qBmFV2:disabled + label::before {
            border: 1px solid rgba(227, 227, 227, 0.2) !important;
            background-color: rgba(227, 227, 227, 0.2) !important;
        }</style><script type="application/json" id="client-env">{"locale":"en","featureFlags":["ab_test_homepage_what_is_copilot_video","code_vulnerability_scanning","copilot_beta_features_opt_in","copilot_chat_conversation_intent_knowledge_search_skill","copilot_chat_static_thread_suggestions","copilot_completion_new_domain","copilot_conversational_ux_history_refs","copilot_copy_message","copilot_followup_to_agent","copilot_implicit_context","copilot_smell_icebreaker_ux","custom_inp","experimentation_azure_variant_endpoint","failbot_handle_non_errors","filter_prefetch_suggestions","geojson_azure_maps","ghost_pilot_confidence_truncation_25","ghost_pilot_confidence_truncation_40","ghost_pilot_stream_handling","hovercard_accessibility","hovercard_longer_activate_timeout","marketing_pages_search_explore_provider","primer_react_css_modules_ga","remove_child_patch","repository_suggester_elastic_search","sample_network_conn_type","site_metered_billing_update"]}</script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_remote-form_dist_index_js-node_modules_delegated-events_dist_inde-fddfb8-5cf727a080bf.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_mini-throttle_dist_decorators_js-node_modules_scroll-anchoring_di-087b76-e6a5ec1d5a5c.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/app_assets_modules_github_diffs_blob-lines_ts-app_assets_modules_github_diffs_linkable-line-n-e2d8d7-57be3d190df1.js.download"></script><script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/diffs-65ebe1b18d4a.js.download"></script><style type="text/css" id="ms-consent-banner-theme-styles"></style><link rel="dns-prefetch" href="https://github.githubassets.com/"><link rel="dns-prefetch" href="https://avatars.githubusercontent.com/"><link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com/"><link rel="dns-prefetch" href="https://user-images.githubusercontent.com/"><link rel="preconnect" href="https://github.githubassets.com/" crossorigin=""><link rel="preconnect" href="https://avatars.githubusercontent.com/"><title>Add files via upload · NTNirjana/session-2--fastapi@c653b67</title><meta name="route-pattern" content="/_view_fragments/Voltron::CommitFragmentsController/show/:user_id/:repository/:name/repo_layout(.:format)" data-turbo-transient=""><meta name="route-controller" content="voltron_commit_fragments" data-turbo-transient=""><meta name="route-action" content="repo_layout" data-turbo-transient=""><meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb"><meta name="request-id" content="179F:33DDD5:AD8D7E:C32589:66D37AA3" data-turbo-transient="true"><meta name="html-safe-nonce" content="54a34ec93e9b296ade650a520accfc365642ae5427de604582b3f259925e5c3d" data-turbo-transient="true"><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9OVE5pcmphbmEvc2Vzc2lvbi0yLS1mYXN0YXBpL3RyZWUvYzY1M2I2Nzc5ZjNiOWQ4ZjBlODI0MjhkNDViNjY1Y2VlZTU0YTY4YyIsInJlcXVlc3RfaWQiOiIxNzlGOjMzRERENTpBRDhEN0U6QzMyNTg5OjY2RDM3QUEzIiwidmlzaXRvcl9pZCI6IjY5MDU5OTg3OTQ1MTI5ODQyNTkiLCJyZWdpb25fZWRnZSI6InNvdXRoZWFzdGFzaWEiLCJyZWdpb25fcmVuZGVyIjoiaWFkIn0=" data-turbo-transient="true"><meta name="visitor-hmac" content="5825b79972ef22d7a4e733a872f4fbf845a34e54c509aae0b1b1a8b1075f4afe" data-turbo-transient="true"><meta name="hovercard-subject-tag" content="repository:844564190" data-turbo-transient=""><meta name="github-keyboard-shortcuts" content="repository,commits,copilot" data-turbo-transient="true"><meta name="selected-link" value="repo_commits" data-turbo-transient=""><link rel="assets" href="https://github.githubassets.com/"><meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I"><meta name="octolytics-url" content="https://collector.github.com/github/collect"><meta name="octolytics-actor-id" content="119169570"><meta name="octolytics-actor-login" content="c193249Tasnia"><meta name="octolytics-actor-hash" content="4aa207626c7288acc9275742cb0d635a1b2d4944a01d5e45557163cf6a8340f1"><meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/voltron/commit_fragments/repo_layout" data-turbo-transient="true"><meta name="user-login" content="c193249Tasnia"><link rel="sudo-modal" href="https://github.com/sessions/sudo_modal"><meta name="turbo-cache-control" content="no-preview" data-turbo-transient=""><link href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c.diff" rel="alternate" type="text/plain+diff" data-turbo-transient="true"><link href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c.patch" rel="alternate" type="text/plain+patch" data-turbo-transient="true"><meta name="diff-view" content="unified" data-turbo-transient=""><meta name="voltron-timing" value="172"><meta name="go-import" content="github.com/NTNirjana/session-2--fastapi git https://github.com/NTNirjana/session-2--fastapi.git"><meta name="octolytics-dimension-user_id" content="119044685"><meta name="octolytics-dimension-user_login" content="NTNirjana"><meta name="octolytics-dimension-repository_id" content="844564190"><meta name="octolytics-dimension-repository_nwo" content="NTNirjana/session-2--fastapi"><meta name="octolytics-dimension-repository_public" content="true"><meta name="octolytics-dimension-repository_is_fork" content="false"><meta name="octolytics-dimension-repository_network_root_id" content="844564190"><meta name="octolytics-dimension-repository_network_root_nwo" content="NTNirjana/session-2--fastapi"><meta name="turbo-body-classes" content="logged-in env-production page-responsive"><meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats"><meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors"><link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000"><link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png"><link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg"><meta name="theme-color" content="#1e2327"><meta name="color-scheme" content="light dark"><link rel="manifest" href="https://github.com/manifest.json" crossorigin="use-credentials"><style type="text/css" id="ms-consent-banner-theme-styles"></style></head>

  <body class="logged-in env-production page-responsive full-width" style="overflow-wrap: break-word; --dialog-scrollgutter: 17px;">
    <div data-turbo-body="" class="logged-in env-production page-responsive" style="word-wrap: break-word;">
      


    <div class="position-relative js-header-wrapper ">
      <a href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c#start-of-content" data-skip-target-assigned="false" class="p-3 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      
      <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/react-lib-7b7b5264f6c1.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_mini-throttle_dist_index_js-node_modules_primer_octicons-react_di-b40d97-2d816f3aa913.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Box_Box_js-55a9038b54f0.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Button_Button_js-b0edbfb6a9e5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_TooltipV2_Tooltip_js-4d5019830e3c.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_node_modules_primer_octicons-react_dist_index_esm_mjs-a5155473fc69.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_ActionList_index_js-fd5a7039f225.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_github_hotkey_dist_index_js-node_modules_lodash-es_capitalize_js-1aaea04d3ac5.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_Dialog_Dialog_js-node_modules_primer_react_lib-esm_-d42c64-94dad1290f54.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/ui_packages_react-core_create-browser-history_ts-ui_packages_safe-storage_safe-storage_ts-ui_-682c2c-40bb20608465.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/ui_packages_ui-commands_ui-commands_ts-f6ad1a8f539f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/keyboard-shortcuts-dialog-a84d01efac8c.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/primer-react-css.8570b2718b0a9c0c8387.module.css">

<react-partial partial-name="keyboard-shortcuts-dialog" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r1f:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>




      

          

                <header class="AppHeader" role="banner">
  <h2 class="sr-only">Navigation Menu</h2>

    

    <div class="AppHeader-globalBar pb-2 js-global-bar">
      <div class="AppHeader-globalBar-start">
          <deferred-side-panel data-url="/_side-panels/global" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <button aria-label="Open global navigation menu" data-action="click:deferred-side-panel#loadPanel click:deferred-side-panel#panelOpened" data-show-dialog-id="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1" id="dialog-show-dialog-fc3ae65d-5e28-449e-b307-c1277758bda1" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-bg-transparent p-0 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-three-bars Button-visual">
    <path d="M1 2.75A.75.75 0 0 1 1.75 2h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 2.75Zm0 5A.75.75 0 0 1 1.75 7h12.5a.75.75 0 0 1 0 1.5H1.75A.75.75 0 0 1 1 7.75ZM1.75 12h12.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Z"></path>
</svg>
</button>

<dialog-helper>
  <dialog data-target="deferred-side-panel.panel" id="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1" aria-modal="true" aria-labelledby="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1-title" aria-describedby="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade Overlay--placement-left SidePanel">
    <div styles="flex-direction: row;" data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1-title">
        Global navigation
      </h1>
            <div data-view-component="true" class="d-flex">
      <div data-view-component="true" class="AppHeader-logo position-relative">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
</div></div>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="dialog-fc3ae65d-5e28-449e-b307-c1277758bda1-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body d-flex flex-column px-2">    <div data-view-component="true" class="d-flex flex-column mb-3">
        <nav aria-label="Site navigation" data-view-component="true" class="ActionList">
  
  <nav-list data-catalyst="">
    <ul data-target="nav-list.topLevelList" data-view-component="true" class="ActionListWrap">
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g d" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;HOME&quot;,&quot;label&quot;:null}" id="item-7e9cf610-7dce-494b-9cae-db4d2d529a5f" href="https://github.com/dashboard" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-home">
    <path d="M6.906.664a1.749 1.749 0 0 1 2.187 0l5.25 4.2c.415.332.657.835.657 1.367v7.019A1.75 1.75 0 0 1 13.25 15h-3.5a.75.75 0 0 1-.75-.75V9H7v5.25a.75.75 0 0 1-.75.75h-3.5A1.75 1.75 0 0 1 1 13.25V6.23c0-.531.242-1.034.657-1.366l5.25-4.2Zm1.25 1.171a.25.25 0 0 0-.312 0l-5.25 4.2a.25.25 0 0 0-.094.196v7.019c0 .138.112.25.25.25H5.5V8.25a.75.75 0 0 1 .75-.75h3.5a.75.75 0 0 1 .75.75v5.25h2.75a.25.25 0 0 0 .25-.25V6.23a.25.25 0 0 0-.094-.195Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Home
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES&quot;,&quot;label&quot;:null}" id="item-e86ece60-6538-404c-986b-e93834d32828" href="https://github.com/issues" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS&quot;,&quot;label&quot;:null}" id="item-3ba21ef1-4bad-4c58-8455-e0f4071601c6" href="https://github.com/pulls" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PROJECTS&quot;,&quot;label&quot;:null}" id="item-b940d0d5-80b0-4a07-9690-e03e475b392b" href="https://github.com/projects" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;DISCUSSIONS&quot;,&quot;label&quot;:null}" id="item-6804a337-0b34-4d5c-baf8-6864bf56f697" href="https://github.com/discussions" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-comment-discussion">
    <path d="M1.75 1h8.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 10.25 10H7.061l-2.574 2.573A1.458 1.458 0 0 1 2 11.543V10h-.25A1.75 1.75 0 0 1 0 8.25v-5.5C0 1.784.784 1 1.75 1ZM1.5 2.75v5.5c0 .138.112.25.25.25h1a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h3.5a.25.25 0 0 0 .25-.25v-5.5a.25.25 0 0 0-.25-.25h-8.5a.25.25 0 0 0-.25.25Zm13 2a.25.25 0 0 0-.25-.25h-.5a.75.75 0 0 1 0-1.5h.5c.966 0 1.75.784 1.75 1.75v5.5A1.75 1.75 0 0 1 14.25 12H14v1.543a1.458 1.458 0 0 1-2.487 1.03L9.22 12.28a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l2.22 2.22v-2.19a.75.75 0 0 1 .75-.75h1a.25.25 0 0 0 .25-.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Discussions
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;CODESPACES&quot;,&quot;label&quot;:null}" id="item-c0bdef6d-7372-4a32-a2d0-9642074075c9" href="https://github.com/codespaces" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-codespaces">
    <path d="M0 11.25c0-.966.784-1.75 1.75-1.75h12.5c.966 0 1.75.784 1.75 1.75v3A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25Zm2-9.5C2 .784 2.784 0 3.75 0h8.5C13.216 0 14 .784 14 1.75v5a1.75 1.75 0 0 1-1.75 1.75h-8.5A1.75 1.75 0 0 1 2 6.75Zm1.75-.25a.25.25 0 0 0-.25.25v5c0 .138.112.25.25.25h8.5a.25.25 0 0 0 .25-.25v-5a.25.25 0 0 0-.25-.25Zm-2 9.5a.25.25 0 0 0-.25.25v3c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25v-3a.25.25 0 0 0-.25-.25Z"></path><path d="M7 12.75a.75.75 0 0 1 .75-.75h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Codespaces
</span>      
</a>
  
</li>

        
          <li role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;EXPLORE&quot;,&quot;label&quot;:null}" id="item-e82827fc-c670-4338-8121-3493cb837a26" href="https://github.com/explore" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-telescope">
    <path d="M14.184 1.143v-.001l1.422 2.464a1.75 1.75 0 0 1-.757 2.451L3.104 11.713a1.75 1.75 0 0 1-2.275-.702l-.447-.775a1.75 1.75 0 0 1 .53-2.32L11.682.573a1.748 1.748 0 0 1 2.502.57Zm-4.709 9.32h-.001l2.644 3.863a.75.75 0 1 1-1.238.848l-1.881-2.75v2.826a.75.75 0 0 1-1.5 0v-2.826l-1.881 2.75a.75.75 0 1 1-1.238-.848l2.049-2.992a.746.746 0 0 1 .293-.253l1.809-.87a.749.749 0 0 1 .944.252ZM9.436 3.92h-.001l-4.97 3.39.942 1.63 5.42-2.61Zm3.091-2.108h.001l-1.85 1.26 1.505 2.605 2.016-.97a.247.247 0 0 0 .13-.151.247.247 0 0 0-.022-.199l-1.422-2.464a.253.253 0 0 0-.161-.119.254.254 0 0 0-.197.038ZM1.756 9.157a.25.25 0 0 0-.075.33l.447.775a.25.25 0 0 0 .325.1l1.598-.769-.83-1.436-1.465 1Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Explore
</span>      
</a>
  
</li>

        
          
<li data-item-id="" data-targets="nav-list.items" data-view-component="true" class="ActionListItem">
    
    
    <a data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;MARKETPLACE&quot;,&quot;label&quot;:null}" id="item-88529506-acde-4c76-bfc2-809cbe71e57a" href="https://github.com/marketplace" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-gift">
    <path d="M2 2.75A2.75 2.75 0 0 1 4.75 0c.983 0 1.873.42 2.57 1.232.268.318.497.668.68 1.042.183-.375.411-.725.68-1.044C9.376.42 10.266 0 11.25 0a2.75 2.75 0 0 1 2.45 4h.55c.966 0 1.75.784 1.75 1.75v2c0 .698-.409 1.301-1 1.582v4.918A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V9.332C.409 9.05 0 8.448 0 7.75v-2C0 4.784.784 4 1.75 4h.55c-.192-.375-.3-.8-.3-1.25ZM7.25 9.5H2.5v4.75c0 .138.112.25.25.25h4.5Zm1.5 0v5h4.5a.25.25 0 0 0 .25-.25V9.5Zm0-4V8h5.5a.25.25 0 0 0 .25-.25v-2a.25.25 0 0 0-.25-.25Zm-7 0a.25.25 0 0 0-.25.25v2c0 .138.112.25.25.25h5.5V5.5h-5.5Zm3-4a1.25 1.25 0 0 0 0 2.5h2.309c-.233-.818-.542-1.401-.878-1.793-.43-.502-.915-.707-1.431-.707ZM8.941 4h2.309a1.25 1.25 0 0 0 0-2.5c-.516 0-1 .205-1.43.707-.337.392-.646.975-.879 1.793Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Marketplace
</span>      
</a>
  
</li>

</ul>  </nav-list>
</nav>

        <div data-view-component="true" class="my-3 d-flex flex-justify-center height-full">
          <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>  <span class="spinner-screenreader-text sr-only">Loading</span>

</div>
</div>
      <div data-view-component="true" class="flex-1"></div>


      <div data-view-component="true" class="px-2">      <p class="color-fg-subtle text-small text-light">© 2024 GitHub, Inc.</p>

      <div data-view-component="true" class="d-flex flex-wrap text-small text-light">
          <a target="_blank" href="https://github.com/about" data-view-component="true" class="Link mr-2">About</a>
          <a target="_blank" href="https://github.blog/" data-view-component="true" class="Link mr-2">Blog</a>
          <a target="_blank" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link mr-2">Terms</a>
          <a target="_blank" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link mr-2">Privacy</a>
          <a target="_blank" href="https://github.com/security" data-view-component="true" class="Link mr-2">Security</a>
          <a target="_blank" href="https://www.githubstatus.com/" data-view-component="true" class="Link mr-3">Status</a>

</div></div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

  </include-fragment>
</deferred-side-panel>

        <a class="AppHeader-logo ml-2" href="https://github.com/" data-hotkey="g d" aria-label="Homepage " data-turbo="false" data-analytics-event="{&quot;category&quot;:&quot;Header&quot;,&quot;action&quot;:&quot;go to dashboard&quot;,&quot;label&quot;:&quot;icon:logo&quot;}">
          <svg height="32" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github v-align-middle color-fg-default">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
        </a>

          <div class="AppHeader-context">
  <div class="AppHeader-context-compact">
      <button aria-expanded="false" aria-haspopup="dialog" aria-label="Page context: NTNirjana / session-2--fastapi" id="dialog-show-context-region-dialog" data-show-dialog-id="context-region-dialog" type="button" data-view-component="true" class="AppHeader-context-compact-trigger Truncate Button--secondary Button--medium Button box-shadow-none">  <span class="Button-content">
    <span class="Button-label"><span class="AppHeader-context-compact-lead">
                <span class="AppHeader-context-compact-parentItem">NTNirjana</span>
                <span class="no-wrap">&nbsp;/</span>

            </span>

            <strong class="AppHeader-context-compact-mainItem d-flex flex-items-center Truncate">
  <span class="Truncate-text ">session-2--fastapi</span>

</strong></span>
  </span>
</button>

<dialog-helper>
  <dialog id="context-region-dialog" aria-modal="true" aria-labelledby="context-region-dialog-title" aria-describedby="context-region-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="context-region-dialog-title">
        Navigate back to
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="context-region-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="context-region-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">          <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;NTNirjana&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/NTNirjana" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-person mr-1">
    <path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-8.99 0 .75.75 0 0 1-1.498-.07 6.004 6.004 0 0 1 3.431-5.142 3.999 3.999 0 1 1 5.123 0ZM10.5 5a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>

          NTNirjana
        </span>

</a>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;session-2--fastapi&quot;,&quot;screen_size&quot;:&quot;compact&quot;}" href="https://github.com/NTNirjana/session-2--fastapi" data-view-component="true" class="Link--primary Truncate d-flex flex-items-center py-1">
        <span class="AppHeader-context-item-label Truncate-text ">
            <svg aria-hidden="true" height="12" viewBox="0 0 16 16" version="1.1" width="12" data-view-component="true" class="octicon octicon-repo mr-1">
    <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
</svg>

          session-2--fastapi
        </span>

</a>
    </li>
</ul>

</div>
      </scrollable-region>
      
</dialog></dialog-helper>
  </div>

  <div class="AppHeader-context-full">
    <nav role="navigation" aria-label="Page context">
      <ul role="list" class="list-style-none">
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;NTNirjana&quot;,&quot;screen_size&quot;:&quot;full&quot;}" data-hovercard-type="user" data-hovercard-url="/users/NTNirjana/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NTNirjana" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          NTNirjana
        </span>

</a>
        <span class="AppHeader-context-item-separator">/</span>
    </li>
    <li>
      <a data-analytics-event="{&quot;category&quot;:&quot;SiteHeaderComponent&quot;,&quot;action&quot;:&quot;context_region_crumb&quot;,&quot;label&quot;:&quot;session-2--fastapi&quot;,&quot;screen_size&quot;:&quot;full&quot;}" href="https://github.com/NTNirjana/session-2--fastapi" data-view-component="true" class="AppHeader-context-item">
        <span class="AppHeader-context-item-label  ">

          session-2--fastapi
        </span>

</a>
    </li>
</ul>

    </nav>
  </div>
</div>

      </div>
      <div class="AppHeader-globalBar-end">
          <div class="AppHeader-search">
              


<qbsearch-input class="search-input" data-scope="repo:NTNirjana/session-2--fastapi" data-custom-scopes-path="/search/custom_scopes" data-delete-custom-scopes-csrf="kKHvyi9rL9CK8xj-ibwMww8Ca_Gt9Mi-lp7S2DPMeqOsXYpbZFtRbpf5l0vGu0FWealpaUhjX99e5QsLk63ePQ" data-max-custom-scopes="10" data-header-redesign-enabled="true" data-initial-value="" data-blackbird-suggestions-path="/search/suggestions" data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations" data-current-repository="NTNirjana/session-2--fastapi" data-current-org="" data-current-owner="NTNirjana" data-logged-in="true" data-copilot-chat-enabled="false" data-nl-search-enabled="false" data-catalyst="">
  <div class="search-input-container search-with-dialog position-relative d-flex flex-row flex-items-center height-auto color-bg-transparent border-0 color-fg-subtle mx-0" data-action="click:qbsearch-input#searchInputContainerClicked">
      
            <button type="button" data-action="click:qbsearch-input#handleExpand" class="AppHeader-button AppHeader-search-whenNarrow" aria-label="Search or jump to…" aria-expanded="false" aria-haspopup="dialog">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </button>


<div class="AppHeader-search-whenRegular">
  <div class="AppHeader-search-wrap AppHeader-search-wrap--hasTrailing">
    <div class="AppHeader-search-control">
      <label for="AppHeader-searchInput" aria-label="Search or jump to…" class="AppHeader-search-visual--leading">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
      </label>

                <button type="button" data-target="qbsearch-input.inputButton" data-action="click:qbsearch-input#handleExpand" class="AppHeader-searchButton form-control input-contrast text-left color-fg-subtle no-wrap placeholder" data-hotkey="s,/" data-analytics-event="{&quot;location&quot;:&quot;navbar&quot;,&quot;action&quot;:&quot;searchbar&quot;,&quot;context&quot;:&quot;global&quot;,&quot;tag&quot;:&quot;input&quot;,&quot;label&quot;:&quot;searchbar_input_global_navbar&quot;}" aria-describedby="search-error-message-flash">
            <div class="overflow-hidden">
              <span id="qb-input-query" data-target="qbsearch-input.inputButtonText">
                  Type <kbd class="AppHeader-search-kbd">/</kbd> to search
              </span>
            </div>
          </button>

    </div>


  </div>
</div>

    <input type="hidden" name="type" class="js-site-search-type-field">

    
<div class="Overlay--hidden " data-modal-dialog-overlay="">
  <modal-dialog data-action="close:qbsearch-input#handleClose cancel:qbsearch-input#handleClose" data-target="qbsearch-input.searchSuggestionsDialog" role="dialog" id="search-suggestions-dialog" aria-modal="true" aria-labelledby="search-suggestions-dialog-header" data-view-component="true" class="Overlay Overlay--width-medium Overlay--height-auto">
      <h1 id="search-suggestions-dialog-header" class="sr-only">Search code, repositories, users, issues, pull requests...</h1>
    <div class="Overlay-body Overlay-body--paddingNone">
      
          <div data-view-component="true">        <div class="search-suggestions position-absolute width-full color-shadow-large border color-fg-default color-bg-default overflow-hidden d-flex flex-column query-builder-container" style="border-radius: 12px;" data-target="qbsearch-input.queryBuilderContainer" hidden="">
          <!-- '"` --><!-- </textarea></xmp> --><form id="query-builder-test-form" action="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c" accept-charset="UTF-8" method="get">
  <query-builder data-target="qbsearch-input.queryBuilder" id="query-builder-query-builder-test" data-filter-key=":" data-view-component="true" class="QueryBuilder search-query-builder" data-min-width="300" data-catalyst="">
    <div class="FormControl FormControl--fullWidth">
      <label id="query-builder-test-label" for="query-builder-test" class="FormControl-label sr-only">
        Search
      </label>
      <div class="QueryBuilder-StyledInput width-fit " data-target="query-builder.styledInput">
          <span id="query-builder-test-leadingvisual-wrap" class="FormControl-input-leadingVisualWrap QueryBuilder-leadingVisualWrap">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-search FormControl-input-leadingVisual">
    <path d="M10.68 11.74a6 6 0 0 1-7.922-8.982 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z"></path>
</svg>
          </span>
        <div data-target="query-builder.styledInputContainer" class="QueryBuilder-StyledInputContainer">
          <div aria-hidden="true" class="QueryBuilder-StyledInputContent" data-target="query-builder.styledInputContent"></div>
          <div class="QueryBuilder-InputWrapper">
            <div aria-hidden="true" class="QueryBuilder-Sizer" data-target="query-builder.sizer"><span></span></div>
            <input id="query-builder-test" name="query-builder-test" value="" autocomplete="off" type="text" role="combobox" spellcheck="false" aria-expanded="false" aria-describedby="validation-212d584b-cced-4617-bfe7-7f00a719e5d3" data-target="query-builder.input" data-action="
          input:query-builder#inputChange
          blur:query-builder#inputBlur
          keydown:query-builder#inputKeydown
          focus:query-builder#inputFocus
        " data-view-component="true" class="FormControl-input QueryBuilder-Input FormControl-medium" aria-controls="query-builder-test-results" aria-autocomplete="list" aria-haspopup="listbox" style="width: 300px;">
          </div>
        </div>
          <span class="sr-only" id="query-builder-test-clear">Clear</span>
          <button role="button" id="query-builder-test-clear-button" aria-labelledby="query-builder-test-clear query-builder-test-label" data-target="query-builder.clearButton" data-action="
                click:query-builder#clear
                focus:query-builder#clearButtonFocus
                blur:query-builder#clearButtonBlur
              " variant="small" hidden="" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium mr-1 px-2 py-0 d-flex flex-items-center rounded-1 color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x-circle-fill Button-visual">
    <path d="M2.343 13.657A8 8 0 1 1 13.658 2.343 8 8 0 0 1 2.343 13.657ZM6.03 4.97a.751.751 0 0 0-1.042.018.751.751 0 0 0-.018 1.042L6.94 8 4.97 9.97a.749.749 0 0 0 .326 1.275.749.749 0 0 0 .734-.215L8 9.06l1.97 1.97a.749.749 0 0 0 1.275-.326.749.749 0 0 0-.215-.734L9.06 8l1.97-1.97a.749.749 0 0 0-.326-1.275.749.749 0 0 0-.734.215L8 6.94Z"></path>
</svg>
</button>

      </div>
      <template id="search-icon"></template>

<template id="code-icon"></template>

<template id="file-code-icon"></template>

<template id="history-icon"></template>

<template id="repo-icon"></template>

<template id="bookmark-icon"></template>

<template id="plus-circle-icon"></template>

<template id="circle-icon"></template>

<template id="trash-icon"></template>

<template id="team-icon"></template>

<template id="project-icon"></template>

<template id="pencil-icon"></template>

<template id="copilot-icon"></template>

<template id="copilot-error-icon"></template>

<template id="workflow-icon"></template>

<template id="book-icon"></template>

<template id="code-review-icon"></template>

<template id="codespaces-icon"></template>

<template id="comment-icon"></template>

<template id="comment-discussion-icon"></template>

<template id="organization-icon"></template>

<template id="rocket-icon"></template>

<template id="shield-check-icon"></template>

<template id="heart-icon"></template>

<template id="server-icon"></template>

<template id="globe-icon"></template>

<template id="issue-opened-icon"></template>

<template id="device-mobile-icon"></template>

<template id="package-icon"></template>

<template id="credit-card-icon"></template>

<template id="play-icon"></template>

<template id="gift-icon"></template>

<template id="code-square-icon"></template>

<template id="device-desktop-icon"></template>

        <div class="position-relative">
                <ul role="listbox" class="ActionListWrap QueryBuilder-ListWrap" aria-label="Suggestions" data-action="
                    combobox-commit:query-builder#comboboxCommit
                    mousedown:query-builder#resultsMousedown
                  " data-target="query-builder.resultsList" data-persist-list="false" id="query-builder-test-results"></ul>
        </div>
      <div class="FormControl-inlineValidation" id="validation-212d584b-cced-4617-bfe7-7f00a719e5d3" hidden="hidden">
        <span class="FormControl-inlineValidation--visual">
          <svg aria-hidden="true" height="12" viewBox="0 0 12 12" version="1.1" width="12" data-view-component="true" class="octicon octicon-alert-fill">
    <path d="M4.855.708c.5-.896 1.79-.896 2.29 0l4.675 8.351a1.312 1.312 0 0 1-1.146 1.954H1.33A1.313 1.313 0 0 1 .183 9.058ZM7 7V3H5v4Zm-1 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z"></path>
</svg>
        </span>
        <span></span>
</div>    </div>
    <div data-target="query-builder.screenReaderFeedback" aria-live="polite" aria-atomic="true" class="sr-only">0 suggestions.</div>
</query-builder></form>
          <div class="d-flex flex-row color-fg-muted px-3 text-small color-bg-default search-feedback-prompt">
            <a target="_blank" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax" data-view-component="true" class="Link color-fg-accent text-normal ml-2">
              Search syntax tips
</a>            <div class="d-flex flex-1"></div>
              <button data-action="click:qbsearch-input#showFeedbackDialog" type="button" data-view-component="true" class="Button--link Button--medium Button color-fg-accent text-normal ml-2">  <span class="Button-content">
    <span class="Button-label">Give feedback</span>
  </span>
</button>
          </div>
        </div>
</div>

    </div>
</modal-dialog></div>
  </div>
  <div data-action="click:qbsearch-input#retract" class="dark-backdrop position-fixed" hidden="" data-target="qbsearch-input.darkBackdrop"></div>
  <div class="color-fg-default">
    
<dialog-helper>
  <dialog data-target="qbsearch-input.feedbackDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="feedback-dialog" aria-modal="true" aria-labelledby="feedback-dialog-title" aria-describedby="feedback-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="feedback-dialog-title">
        Provide feedback
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="feedback-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="feedback-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <!-- '"` --><!-- </textarea></xmp> --><form id="code-search-feedback-form" data-turbo="false" action="https://github.com/search/feedback" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="DuMQWUNui_w1UaqRQQZvrbFY7i9vBB7q7I_szRj-sVsg-gHbpiIumlQPCsVTmIx_sJmkTKmjAFUjoHt0WdBmqw">
          <p>We read every piece of feedback, and take your input very seriously.</p>
          <textarea name="feedback" class="form-control width-full mb-2" style="height: 120px" id="feedback"></textarea>
          <input name="include_email" id="include_email" aria-label="Include my email address so I can be contacted" class="form-control mr-2" type="checkbox">
          <label for="include_email" style="font-weight: normal">Include my email address so I can be contacted</label>
</form></div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd">          <button data-close-dialog-id="feedback-dialog" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="code-search-feedback-form" data-action="click:qbsearch-input#submitFeedback" type="submit" data-view-component="true" class="btn-primary btn">    Submit feedback
</button>
</div>
</dialog></dialog-helper>

    <custom-scopes data-target="qbsearch-input.customScopesManager" data-catalyst="">
    
<dialog-helper>
  <dialog data-target="custom-scopes.customScopesModalDialog" data-action="close:qbsearch-input#handleDialogClose cancel:qbsearch-input#handleDialogClose" id="custom-scopes-dialog" aria-modal="true" aria-labelledby="custom-scopes-dialog-title" aria-describedby="custom-scopes-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade">
    <div data-view-component="true" class="Overlay-header Overlay-header--divided">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="custom-scopes-dialog-title">
        Saved searches
      </h1>
        <h2 id="custom-scopes-dialog-description" class="Overlay-description">Use saved searches to filter your results more quickly</h2>
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="custom-scopes-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="custom-scopes-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

        <div hidden="" class="create-custom-scope-form" data-target="custom-scopes.createCustomScopeForm">
        <!-- '"` --><!-- </textarea></xmp> --><form id="custom-scopes-dialog-form" data-turbo="false" action="https://github.com/search/custom_scopes" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="pUuKSHsxXXli20ysom65hVXHsH-cp_Sdxzm0I9vzBaOWVTV9CthwHr0nzgts1bOcqih8AgyNoDAbT-Ouxj2dyg">
          <div data-target="custom-scopes.customScopesModalDialogFlash"></div>

          <input type="hidden" id="custom_scope_id" name="custom_scope_id" data-target="custom-scopes.customScopesIdField">

          <div class="form-group">
            <label for="custom_scope_name">Name</label>
            <auto-check src="/search/custom_scopes/check_name" required="">
              <input type="text" name="custom_scope_name" id="custom_scope_name" data-target="custom-scopes.customScopesNameField" class="form-control" autocomplete="off" placeholder="github-ruby" required="" maxlength="50" spellcheck="false">
              <input type="hidden" value="KdtvVLxPR4bsVnPPza8DkyRH97QxoQXW3Z2YTTbi_Nei9-21Mv2kX4ni7soPymrsdOzdCPy_uTuZ_sTMH1_-1A" data-csrf="true">
            </auto-check>
          </div>

          <div class="form-group">
            <label for="custom_scope_query">Query</label>
            <input type="text" name="custom_scope_query" id="custom_scope_query" data-target="custom-scopes.customScopesQueryField" class="form-control" autocomplete="off" placeholder="(repo:mona/a OR repo:mona/b) AND lang:python" required="" maxlength="500">
          </div>

          <p class="text-small color-fg-muted">
            To see all available qualifiers, see our <a class="Link--inTextBlock" href="https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax">documentation</a>.
          </p>
</form>        </div>

        <div data-target="custom-scopes.manageCustomScopesForm">
          <div data-target="custom-scopes.list"></div>
        </div>

</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">          <button data-action="click:custom-scopes#customScopesCancel" type="button" data-view-component="true" class="btn">    Cancel
</button>
          <button form="custom-scopes-dialog-form" data-action="click:custom-scopes#customScopesSubmit" data-target="custom-scopes.customScopesSubmitButton" type="submit" data-view-component="true" class="btn-primary btn">    Create saved search
</button>
</div>
</dialog></dialog-helper>
    </custom-scopes>
  </div>
</qbsearch-input>    <input type="hidden" value="jdy_NPGDM6UiIhKbqqlXEBIXdOLeYCMNzRGetU_mTL4rmfQpYxKfLtEHaAJKkaiw2U8Gc-hGgWqv2rnRuLS8tQ" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf">

          </div>

        <div class="AppHeader-actions position-relative">
             <react-partial-anchor data-catalyst="">
      <button id="global-create-menu-anchor" aria-label="Create something new" data-target="react-partial-anchor.anchor" type="button" data-view-component="true" class="AppHeader-button global-create-button Button--secondary Button--medium Button width-auto color-fg-muted" aria-describedby="tooltip-c3eaad87-1375-4580-b2d2-05031f060dca" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
    <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
</svg></span>
  </span>
</button><tool-tip id="tooltip-c3eaad87-1375-4580-b2d2-05031f060dca" for="global-create-menu-anchor" popover="manual" data-direction="s" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Create new...</tool-tip>

      
    
        <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_ActionMenu_ActionMenu_js-node_modules_primer_react_-5b2420-50d72766db7f.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/vendors-node_modules_primer_react_lib-esm_FeatureFlags_FeatureFlags_js-node_modules_primer_re-7faff4-1dd74dc0d752.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/ui_packages_react-core_register-partial_ts-ui_packages_global-create-menu_GlobalCreateMenu_tsx-4fb134843007.js.download"></script>
<script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/global-create-menu-f5f67baa8031.js.download"></script>

<react-partial partial-name="global-create-menu" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"createRepo":true,"importRepo":true,"codespaces":true,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/c193249Tasnia?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"NTNirjana","repo":"session-2--fastapi"}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r1g:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>

      </react-partial-anchor>


          <a href="https://github.com/issues" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;ISSUES_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-e65be1e8-ce18-4219-8d45-7cfb257b6f8e" aria-labelledby="tooltip-4fcbe0e7-0c4f-4fb9-9425-09e1e483f7e9" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened Button-visual">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
</a><tool-tip id="tooltip-4fcbe0e7-0c4f-4fb9-9425-09e1e483f7e9" for="icon-button-e65be1e8-ce18-4219-8d45-7cfb257b6f8e" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Issues</tool-tip>

          <a href="https://github.com/pulls" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;PULL_REQUESTS_HEADER&quot;,&quot;label&quot;:null}" id="icon-button-586dc894-1586-49fc-9f49-05ceb382f84f" aria-labelledby="tooltip-c44912c3-de3b-4363-bb81-9494e611a5c5" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request Button-visual">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
</a><tool-tip id="tooltip-c44912c3-de3b-4363-bb81-9494e611a5c5" for="icon-button-586dc894-1586-49fc-9f49-05ceb382f84f" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Pull requests</tool-tip>

        </div>

        <notification-indicator data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTE5MTY5NTcwIiwidCI6MTcyNTEzNTUyM30=--6813731d80aa505c8cf27381a56f73b61e5f4c5120d0756fa1923c5abe3c3afc" data-indicator-mode="none" data-tooltip-global="You have unread notifications" data-tooltip-unavailable="Notifications are unavailable at the moment." data-tooltip-none="You have no unread notifications" data-header-redesign-enabled="true" data-fetch-indicator-src="/notifications/indicator" data-fetch-indicator-enabled="true" data-view-component="true" class="js-socket-channel" data-fetch-retry-delay-time="500" data-catalyst="">
    <a id="AppHeader-notifications-button" href="https://github.com/notifications" aria-labelledby="notification-indicator-tooltip" data-hotkey="g n" data-target="notification-indicator.link" data-analytics-event="{&quot;category&quot;:&quot;Global navigation&quot;,&quot;action&quot;:&quot;NOTIFICATIONS_HEADER&quot;,&quot;label&quot;:&quot;icon:read&quot;}" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium AppHeader-button color-fg-muted">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-inbox Button-visual">
    <path d="M2.8 2.06A1.75 1.75 0 0 1 4.41 1h7.18c.7 0 1.333.417 1.61 1.06l2.74 6.395c.04.093.06.194.06.295v4.5A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25v-4.5c0-.101.02-.202.06-.295Zm1.61.44a.25.25 0 0 0-.23.152L1.887 8H4.75a.75.75 0 0 1 .6.3L6.625 10h2.75l1.275-1.7a.75.75 0 0 1 .6-.3h2.863L11.82 2.652a.25.25 0 0 0-.23-.152Zm10.09 7h-2.875l-1.275 1.7a.75.75 0 0 1-.6.3h-3.5a.75.75 0 0 1-.6-.3L4.375 9.5H1.5v3.75c0 .138.112.25.25.25h12.5a.25.25 0 0 0 .25-.25Z"></path>
</svg>
</a>

    <tool-tip id="notification-indicator-tooltip" data-target="notification-indicator.tooltip" for="AppHeader-notifications-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>You have no unread notifications</tool-tip>
</notification-indicator>

        

        <div class="AppHeader-user">
          <deferred-side-panel data-url="/_side-panels/user?repository_id=844564190" data-catalyst="">
  <include-fragment data-target="deferred-side-panel.fragment"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
    <react-partial-anchor data-catalyst="">
  <button data-target="react-partial-anchor.anchor" data-login="c193249Tasnia" aria-label="Open user navigation menu" type="button" data-view-component="true" class="Button--invisible Button--medium Button Button--invisible-noVisuals color-bg-transparent p-0" aria-expanded="false" aria-haspopup="true">  <span class="Button-content">
    <span class="Button-label"><img src="./basic_files/119169570" alt="" size="32" height="32" width="32" data-view-component="true" class="avatar circle"></span>
  </span>
</button>
  

    <script crossorigin="anonymous" defer="defer" type="application/javascript" src="./basic_files/global-user-nav-drawer-a262b436b18b.js.download"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="./basic_files/global-user-nav-drawer.830d6c10c9fea7fc134e.module.css">

<react-partial partial-name="global-user-nav-drawer" data-ssr="false" data-catalyst="" class="loaded">
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"owner":{"login":"c193249Tasnia","name":null,"avatarUrl":"https://avatars.githubusercontent.com/u/119169570?v=4"},"drawerId":"global-user-nav-drawer","lazyLoadItemDataFetchUrl":"/_side-panels/user.json","canAddAccount":true,"addAccountPath":"/login?add_account=1\u0026return_to=https%3A%2F%2Fgithub.com%2FNTNirjana%2Fsession-2--fastapi%2Fcommit%2Fc653b6779f3b9d8f0e82428d45b665ceee54a68c","switchAccountPath":"/switch_account","loginAccountPath":"/login?add_account=1","projectsPath":"/c193249Tasnia?tab=projects","gistsUrl":"https://gist.github.com/mine","docsUrl":"https://docs.github.com","yourEnterpriseUrl":null,"enterpriseSettingsUrl":null,"supportUrl":"https://support.github.com","showAccountSwitcher":true,"showEnterprises":true,"showEnterprise":false,"showGists":true,"showSponsors":true,"showFeaturesPreviews":true,"showEnterpriseSettings":false,"createMenuProps":{"createRepo":true,"importRepo":true,"codespaces":true,"gist":true,"createOrg":true,"createProject":false,"createProjectUrl":"/c193249Tasnia?tab=projects","createLegacyProject":false,"createIssue":false,"org":null,"owner":"NTNirjana","repo":"session-2--fastapi"}}}</script>
  <div data-target="react-partial.reactRoot"><script type="application/json" id="__PRIMER_DATA_:r1j:__">{"resolvedServerColorMode":"day"}</script></div>
</react-partial>

  </react-partial-anchor>

  </include-fragment>
</deferred-side-panel>
        </div>

        <div class="position-absolute mt-2">
            
<site-header-logged-in-user-menu data-catalyst="">

</site-header-logged-in-user-menu>

        </div>
      </div>
    </div>


      <div class="AppHeader-localBar">
        <nav data-pjax="#js-repo-pjax-container" aria-label="Repository" data-view-component="true" class="js-repo-nav js-sidenav-container-pjax js-responsive-underlinenav overflow-hidden UnderlineNav">

  <ul data-view-component="true" class="UnderlineNav-body list-style-none">
      <li data-view-component="true" class="d-inline-flex">
  <a id="code-tab" href="https://github.com/NTNirjana/session-2--fastapi" data-tab-item="i0code-tab" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages repo_deployments repo_attestations /NTNirjana/session-2--fastapi" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g c" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Code&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item selected" aria-current="page">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code UnderlineNav-octicon d-none d-sm-inline">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        <span data-content="Code">Code</span>
          <span id="code-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="issues-tab" href="https://github.com/NTNirjana/session-2--fastapi/issues" data-tab-item="i1issues-tab" data-selected-links="repo_issues repo_labels repo_milestones /NTNirjana/session-2--fastapi/issues /_view_fragments/issues/index/NTNirjana/session-2--fastapi/layout" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g i" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Issues&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        <span data-content="Issues">Issues</span>
          <span id="issues-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="pull-requests-tab" href="https://github.com/NTNirjana/session-2--fastapi/pulls" data-tab-item="i2pull-requests-tab" data-selected-links="repo_pulls checks /NTNirjana/session-2--fastapi/pulls" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g p" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Pull requests&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        <span data-content="Pull requests">Pull requests</span>
          <span id="pull-requests-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="actions-tab" href="https://github.com/NTNirjana/session-2--fastapi/actions" data-tab-item="i3actions-tab" data-selected-links="repo_actions /NTNirjana/session-2--fastapi/actions" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g a" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Actions&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play UnderlineNav-octicon d-none d-sm-inline">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        <span data-content="Actions">Actions</span>
          <span id="actions-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="projects-tab" href="https://github.com/NTNirjana/session-2--fastapi/projects" data-tab-item="i4projects-tab" data-selected-links="repo_projects new_repo_project repo_project /NTNirjana/session-2--fastapi/projects" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g b" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Projects&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table UnderlineNav-octicon d-none d-sm-inline">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        <span data-content="Projects">Projects</span>
          <span id="projects-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="0" hidden="hidden" data-view-component="true" class="Counter">0</span>


    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="security-tab" href="https://github.com/NTNirjana/session-2--fastapi/security" data-tab-item="i5security-tab" data-selected-links="security overview alerts policy token_scanning code_scanning /NTNirjana/session-2--fastapi/security" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-hotkey="g s" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Security&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield UnderlineNav-octicon d-none d-sm-inline">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span data-content="Security">Security</span>
          

    
</a></li>
      <li data-view-component="true" class="d-inline-flex">
  <a id="insights-tab" href="https://github.com/NTNirjana/session-2--fastapi/pulse" data-tab-item="i6insights-tab" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people community /NTNirjana/session-2--fastapi/pulse" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame" data-analytics-event="{&quot;category&quot;:&quot;Underline navbar&quot;,&quot;action&quot;:&quot;Click tab&quot;,&quot;label&quot;:&quot;Insights&quot;,&quot;target&quot;:&quot;UNDERLINE_NAV.TAB&quot;}" data-view-component="true" class="UnderlineNav-item no-wrap js-responsive-underlinenav-item js-selected-navigation-item">
    
              <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph UnderlineNav-octicon d-none d-sm-inline">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        <span data-content="Insights">Insights</span>
          <span id="insights-repo-tab-count" data-pjax-replace="" data-turbo-replace="" title="Not available" data-view-component="true" class="Counter"></span>


    
</a></li>
</ul>
    <div style="visibility:hidden;" data-view-component="true" class="UnderlineNav-actions js-responsive-underlinenav-overflow position-absolute pr-3 pr-md-4 pr-lg-5 right-0">      <action-menu data-select-variant="none" data-view-component="true" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-button" popovertarget="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-overlay" aria-controls="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-list" aria-haspopup="true" aria-labelledby="tooltip-a0218878-dbbf-476d-911f-fec01fc21fe8" type="button" data-view-component="true" class="Button Button--iconOnly Button--secondary Button--medium UnderlineNav-item">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-a0218878-dbbf-476d-911f-fec01fc21fe8" for="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Additional navigation options</tool-tip>


<anchored-position id="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-overlay" anchor="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-button" align="start" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 36px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-button" id="action-menu-279c51c7-f3de-443b-90b9-20c9ca4e50e5-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li hidden="" data-menu-item="i0code-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-2777eda6-19d2-4881-81d6-86c2f7a23daa" href="https://github.com/NTNirjana/session-2--fastapi" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i1issues-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-f132ff8d-2dc9-4b8e-bbdd-664f97124583" href="https://github.com/NTNirjana/session-2--fastapi/issues" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-issue-opened">
    <path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Issues
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i2pull-requests-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-4852a809-6036-4e9e-8510-cee8b6d747ad" href="https://github.com/NTNirjana/session-2--fastapi/pulls" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-pull-request">
    <path d="M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Pull requests
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i3actions-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-4b93c329-6244-465e-b6d5-452666c573af" href="https://github.com/NTNirjana/session-2--fastapi/actions" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-play">
    <path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Zm4.879-2.773 4.264 2.559a.25.25 0 0 1 0 .428l-4.264 2.559A.25.25 0 0 1 6 10.559V5.442a.25.25 0 0 1 .379-.215Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Actions
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i4projects-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-7fd782f1-89f9-43b0-9095-76270c87e2e7" href="https://github.com/NTNirjana/session-2--fastapi/projects" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-table">
    <path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25ZM6.5 6.5v8h7.75a.25.25 0 0 0 .25-.25V6.5Zm8-1.5V1.75a.25.25 0 0 0-.25-.25H6.5V5Zm-13 1.5v7.75c0 .138.112.25.25.25H5v-8ZM5 5V1.5H1.75a.25.25 0 0 0-.25.25V5Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Projects
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i5security-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-b9081c9b-20b3-4efd-917d-d2c7585c876f" href="https://github.com/NTNirjana/session-2--fastapi/security" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-shield">
    <path d="M7.467.133a1.748 1.748 0 0 1 1.066 0l5.25 1.68A1.75 1.75 0 0 1 15 3.48V7c0 1.566-.32 3.182-1.303 4.682-.983 1.498-2.585 2.813-5.032 3.855a1.697 1.697 0 0 1-1.33 0c-2.447-1.042-4.049-2.357-5.032-3.855C1.32 10.182 1 8.566 1 7V3.48a1.75 1.75 0 0 1 1.217-1.667Zm.61 1.429a.25.25 0 0 0-.153 0l-5.25 1.68a.25.25 0 0 0-.174.238V7c0 1.358.275 2.666 1.057 3.86.784 1.194 2.121 2.34 4.366 3.297a.196.196 0 0 0 .154 0c2.245-.956 3.582-2.104 4.366-3.298C13.225 9.666 13.5 8.36 13.5 7V3.48a.251.251 0 0 0-.174-.237l-5.25-1.68ZM8.75 4.75v3a.75.75 0 0 1-1.5 0v-3a.75.75 0 0 1 1.5 0ZM9 10.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Security
</span>      
</a>
  
</li>
        <li hidden="" data-menu-item="i6insights-tab" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <a tabindex="-1" id="item-f16022cb-a3e4-4a60-9b64-30c225cc2ff6" href="https://github.com/NTNirjana/session-2--fastapi/pulse" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-graph">
    <path d="M1.5 1.75V13.5h13.75a.75.75 0 0 1 0 1.5H.75a.75.75 0 0 1-.75-.75V1.75a.75.75 0 0 1 1.5 0Zm14.28 2.53-5.25 5.25a.75.75 0 0 1-1.06 0L7 7.06 4.28 9.78a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042l3.25-3.25a.75.75 0 0 1 1.06 0L10 7.94l4.72-4.72a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Insights
</span>      
</a>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></div>
</nav>
      </div>
</header>


      <div hidden="hidden" data-view-component="true" class="js-stale-session-flash stale-session-flash flash flash-warn flash-full">
  
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
        <span class="js-stale-session-flash-signed-in" hidden="">You signed in with another tab or window. <a class="Link--inTextBlock" href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-signed-out" hidden="">You signed out in another tab or window. <a class="Link--inTextBlock" href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c">Reload</a> to refresh your session.</span>
        <span class="js-stale-session-flash-switched" hidden="">You switched accounts on another tab or window. <a class="Link--inTextBlock" href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c">Reload</a> to refresh your session.</span>

    <button id="icon-button-44e036e5-fb59-4b6e-a917-da4f951106d4" aria-labelledby="tooltip-7ad482df-c105-427b-abd5-dd4f0a467003" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium flash-close js-flash-close">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x Button-visual">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-7ad482df-c105-427b-abd5-dd4f0a467003" for="icon-button-44e036e5-fb59-4b6e-a917-da4f951106d4" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Dismiss alert</tool-tip>


  
</div>
          
    </div>

  <div id="start-of-content" class="show-on-focus"></div>








    <div id="js-flash-container" class="flash-container" data-turbo-replace="">




  <template class="js-flash-template"></template>
</div>


    
    <notification-shelf-watcher data-base-url="https://github.com/notifications/beta/shelf" data-channel="eyJjIjoibm90aWZpY2F0aW9uLWNoYW5nZWQ6MTE5MTY5NTcwIiwidCI6MTcyNTEzNTUyM30=--6813731d80aa505c8cf27381a56f73b61e5f4c5120d0756fa1923c5abe3c3afc" data-view-component="true" class="js-socket-channel" data-refresh-delay="500" data-catalyst=""></notification-shelf-watcher>
  <div hidden="" data-initial="" data-target="notification-shelf-watcher.placeholder"></div>






  <div class="application-main " data-commit-hovercards-enabled="" data-discussion-hovercards-enabled="" data-issue-and-pr-hovercards-enabled="">
        <div itemscope="" itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main id="js-repo-pjax-container">
      
  

    






    
  <div id="repository-container-header" data-turbo-replace="" hidden=""></div>




<turbo-frame id="repo-content-turbo-frame" target="_top" data-turbo-action="advance" class="">
    <div id="repo-content-pjax-container" class="repository-content ">
    



    
      
<div class="clearfix container-xl px-3 px-md-4 px-lg-5 mt-4">
  <div class="Subhead">
  <h2 class="Subhead-heading">Commit</h2>
</div>

<a href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>




<div id="spoof-warning" class="mt-0 pb-3" hidden="" aria-hidden="">
  <div data-view-component="true" class="flash flash-warn mt-0 clearfix">
  
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert float-left mt-1">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>

      <div class="overflow-hidden">This commit does not belong to any branch on this repository, and may belong to a fork outside of the repository.</div>


  
</div></div>


<div class="commit full-commit mt-0 px-2 pt-2 ">
  <div class="d-flex flex-justify-between gap-2">
    <div class="d-flex">
        <span class="mr-1" style="height: 24px">
        </span>

        <div class="commit-title markdown-title">
          Add files via upload
        </div>
    </div>

    <a id="browse-at-time-link" href="https://github.com/NTNirjana/session-2--fastapi/tree/c653b6779f3b9d8f0e82428d45b665ceee54a68c" class="btn flex-self-start" rel="nofollow" aria-describedby="tooltip-c75fda59-3aad-4006-a70b-98b83be99706">Browse files</a>
    <tool-tip id="tooltip-c75fda59-3aad-4006-a70b-98b83be99706" for="browse-at-time-link" popover="manual" data-direction="ne" data-type="description" data-view-component="true" class="sr-only position-absolute" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Browse the repository at this point in the history</tool-tip>
  </div>


  <div class="commit-branches pb-2">
  

    <div class="pt-2">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-git-branch">
    <path d="M9.5 3.25a2.25 2.25 0 1 1 3 2.122V6A2.5 2.5 0 0 1 10 8.5H6a1 1 0 0 0-1 1v1.128a2.251 2.251 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.5 0v1.836A2.493 2.493 0 0 1 6 7h4a1 1 0 0 0 1-1v-.628A2.25 2.25 0 0 1 9.5 3.25Zm-6 0a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Zm8.25-.75a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5ZM4.25 12a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Z"></path>
</svg>
      <ul class="branches-list">
          <li class="branch"><a href="https://github.com/NTNirjana/session-2--fastapi">main</a></li>
      </ul>
    </div>
</div>


  <div class="commit-meta p-2 d-flex flex-wrap gap-3 flex-column flex-md-row">

    <div class="d-flex flex-1">
      
<div class="AvatarStack flex-self-start  ">
  <div class="AvatarStack-body">
      <a class="avatar avatar-user" style="width:20px;height:20px;" data-test-selector="commits-avatar-stack-avatar-link" data-hovercard-type="user" data-hovercard-url="/users/NTNirjana/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NTNirjana">
        <img data-test-selector="commits-avatar-stack-avatar-image" src="https://avatars.githubusercontent.com/u/119044685?s=40&amp;v=4" width="20" height="20" alt="@NTNirjana" class=" avatar-user">
</a>  </div>
</div>

      <div class="flex-self-start flex-content-center">
            <a class="commit-author user-mention" title="View all commits by NTNirjana" data-hovercard-type="user" data-hovercard-url="/users/NTNirjana/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/NTNirjana/session-2--fastapi/commits?author=NTNirjana">NTNirjana</a>
    
  committed
  <relative-time datetime="2024-08-19T14:15:00Z" class="no-wrap" title="Aug 19, 2024, 8:15 PM GMT+6"><template shadowrootmode="open">2 weeks ago</template>Aug 19, 2024</relative-time>

        <div class="d-none d-md-inline-block">
          

    <button id="dialog-show-commit-badge-verified-f30ba0c1-dialog" data-show-dialog-id="commit-badge-verified-f30ba0c1-dialog" type="button" data-view-component="true" class="signed-commit-badge signed-commit-badge-medium verified  Button--secondary Button--medium Button">  <span class="Button-content">
    <span class="Button-label">Verified</span>
  </span>
</button>

<dialog-helper>
  <dialog id="commit-badge-verified-f30ba0c1-dialog" aria-modal="true" aria-labelledby="commit-badge-verified-f30ba0c1-dialog-title" aria-describedby="commit-badge-verified-f30ba0c1-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-small-portrait Overlay--motion-scaleFade">
    <div style="border-radius: 12px 12px 0 0" data-view-component="true" class="Overlay-header Overlay-header--divided color-bg-subtle">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title sr-only" id="commit-badge-verified-f30ba0c1-dialog-title">
        Verified
      </h1>
                <div class="d-flex">
          <div class="pr-1">
            <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-verified mr-2 color-fg-success">
    <path d="m9.585.52.929.68c.153.112.331.186.518.215l1.138.175a2.678 2.678 0 0 1 2.24 2.24l.174 1.139c.029.187.103.365.215.518l.68.928a2.677 2.677 0 0 1 0 3.17l-.68.928a1.174 1.174 0 0 0-.215.518l-.175 1.138a2.678 2.678 0 0 1-2.241 2.241l-1.138.175a1.17 1.17 0 0 0-.518.215l-.928.68a2.677 2.677 0 0 1-3.17 0l-.928-.68a1.174 1.174 0 0 0-.518-.215L3.83 14.41a2.678 2.678 0 0 1-2.24-2.24l-.175-1.138a1.17 1.17 0 0 0-.215-.518l-.68-.928a2.677 2.677 0 0 1 0-3.17l.68-.928c.112-.153.186-.331.215-.518l.175-1.14a2.678 2.678 0 0 1 2.24-2.24l1.139-.175c.187-.029.365-.103.518-.215l.928-.68a2.677 2.677 0 0 1 3.17 0ZM7.303 1.728l-.927.68a2.67 2.67 0 0 1-1.18.489l-1.137.174a1.179 1.179 0 0 0-.987.987l-.174 1.136a2.677 2.677 0 0 1-.489 1.18l-.68.928a1.18 1.18 0 0 0 0 1.394l.68.927c.256.348.424.753.489 1.18l.174 1.137c.078.509.478.909.987.987l1.136.174a2.67 2.67 0 0 1 1.18.489l.928.68c.414.305.979.305 1.394 0l.927-.68a2.67 2.67 0 0 1 1.18-.489l1.137-.174a1.18 1.18 0 0 0 .987-.987l.174-1.136a2.67 2.67 0 0 1 .489-1.18l.68-.928a1.176 1.176 0 0 0 0-1.394l-.68-.927a2.686 2.686 0 0 1-.489-1.18l-.174-1.137a1.179 1.179 0 0 0-.987-.987l-1.136-.174a2.677 2.677 0 0 1-1.18-.489l-.928-.68a1.176 1.176 0 0 0-1.394 0ZM11.28 6.78l-3.75 3.75a.75.75 0 0 1-1.06 0L4.72 8.78a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L7 8.94l3.22-3.22a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042Z"></path>
</svg>
          </div>
          <div class="flex-1">
                This commit was created on GitHub.com and signed with GitHub’s <strong class="color-fg-success">verified signature</strong>.
          </div>
        </div>

    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="commit-badge-verified-f30ba0c1-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="commit-badge-verified-f30ba0c1-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">        <div class="signed-commit-footer pt-3">
            <span class="d-block">GPG key ID: <span class="color-fg-muted">B5690EEEBB952194</span></span>
            <div class="my-1">
            </div>
          <a class="Link--inTextBlock" href="https://docs.github.com/github/authenticating-to-github/displaying-verification-statuses-for-all-of-your-commits">Learn about vigilant mode</a>
        </div>
</div>
      </scrollable-region>
      
</dialog></dialog-helper>

        </div>
      </div>
    </div>

    <div class="d-flex gap-3 no-wrap text-lg-right text-left overflow-x-auto">
      <span class="sha-block ml-0" data-pjax="#repo-content-pjax-container" data-turbo-frame="repo-content-turbo-frame">
        0 parents
      </span>
      <span class="sha-block m-0">commit <span class="sha user-select-contain">c653b67</span></span>
    </div>
  </div>
</div>


  
      <template id="js-inline-comments-single-container-template"></template>



  <diff-layout sidebar-hidden="" data-catalyst="">
    <div class="pr-toolbar commit-toolbar mt-n2 color-bg-default d-flex js-sticky-offset-scroll" data-target="diff-layout.diffToolbar">
        <div id="toc" class="d-flex flex-items-center js-details-container Details flex-1 my-2" style="gap: 4px 16px;">
  

    <div>
      Showing
      <strong>1 changed file</strong>
      with
      <strong>112 additions</strong>
      and
      <strong>0 deletions</strong>.
    </div>

  <div class="flex-1"></div>
  <div class="d-flex d-inline-block">
    <!-- '"` --><!-- </textarea></xmp> --><form class="d-flex gap-2 flex-column flex-sm-row flex-items-end" data-turbo="false" action="https://github.com/users/diffview" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="q7EWmCG54bIfufjmC41IGg5bC0--2MelEbZUxv8wogFgMlPqmFrYKaOABFHnLnjaQ2v1yrXZ9szIPN8RdH4AZA">
      <segmented-control data-catalyst="">
  <ul aria-label="Whitespace" role="list" data-view-component="true" class="SegmentedControl--small SegmentedControl">
      <li class="SegmentedControl-item SegmentedControl-item--selected" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="w" value="0" data-action="click:segmented-control#select" aria-current="true" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Whitespace">Whitespace</span>
  </span>
</button>

</li>

      <li class="SegmentedControl-item" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="w" value="1" data-action="click:segmented-control#select" aria-current="false" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Ignore whitespace">Ignore whitespace</span>
  </span>
</button>

</li>

</ul></segmented-control>
      <segmented-control data-catalyst="">
  <ul aria-label="Diff view" role="list" data-view-component="true" class="SegmentedControl--small SegmentedControl">
      <li class="SegmentedControl-item" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="diff" value="split" data-action="click:segmented-control#select" aria-current="false" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Split">Split</span>
  </span>
</button>

</li>

      <li class="SegmentedControl-item SegmentedControl-item--selected" role="listitem" data-targets="segmented-control.items">
  <button data-disable-with="" name="diff" value="unified" data-action="click:segmented-control#select" aria-current="true" type="submit" data-view-component="true" class="Button--invisible Button--small Button Button--invisible-noVisuals">  <span class="Button-content">
    <span class="Button-label" data-content="Unified">Unified</span>
  </span>
</button>

</li>

</ul></segmented-control>
      <input type="hidden" name="old_w" id="old_w" value="0" autocomplete="off" class="form-control">
      <input type="hidden" name="old_diff" id="old_diff" value="unified" autocomplete="off" class="form-control">
</form>  </div>
</div>

    </div>
      <div side="left" responsive="true" data-target="diff-layout.layoutContainer" data-view-component="true" class="Layout Layout--flowRow-until-md Layout--gutter-condensed hx_Layout--sidebar-hidden hx_Layout wants-full-width-container Layout--sidebarPosition-start Layout--sidebarPosition-flowRow-none">
  
  <div data-target="diff-layout.sidebarContainer" data-action="scroll:diff-layout.sidebarContainer#handleSidebarScroll" data-view-component="true" class="Layout-sidebar overflow-y-auto hx_Layout--sidebar js-notification-shelf-offset-top position-sticky p-2" data-original-top="60px" style="top: 60px !important; height: 525px;"></div>
  <div data-target="diff-layout.mainContainer" data-view-component="true" class="Layout-main files-next-bucket">          <a name="diff-stat"></a>
          
<template class="js-comment-button-template"></template>

<div id="files" class="diff-view commentable js-diff-container js-code-nav-container" data-hpc="">


  <div class="container-md js-file-filter-blankslate" data-target="diff-file-filter.blankslate" hidden="">
    
  <div class="blankslate-container">
    <div data-view-component="true" class="blankslate">
      <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-filter blankslate-icon">
    <path d="M2.75 6a.75.75 0 0 0 0 1.5h18.5a.75.75 0 0 0 0-1.5H2.75ZM6 11.75a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H6.75a.75.75 0 0 1-.75-.75Zm4 4.938a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"></path>
</svg>

      <h2 data-view-component="true" class="blankslate-heading">        There are no files selected for viewing
</h2>
      

</div>  </div>
  </div>
  <div class="js-diff-progressive-container">
    <copilot-diff-entry data-file-path="basic.py">
  <div id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-details-container-group="file" class="file js-file js-details-container js-targetable-element show-inline-notes Details
               Details--on open
              
              
              
              
              
              js-tagsearch-file" data-file-type=".py" data-file-deleted="false" data-tagsearch-path="basic.py" data-tagsearch-lang="Python" data-targets="diff-file-filter.diffEntries">
    <div class="file-header d-flex flex-md-row flex-column flex-md-items-center file-header--expandable js-file-header js-skip-tagsearch " data-path="basic.py" data-short-path="f0e899a" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-file-type=".py" data-file-deleted="false">
      <div class="file-info flex-auto min-width-0 mb-md-0 mb-2">
        <button type="button" class="btn-octicon js-details-target" aria-label="Toggle diff contents" aria-expanded="true" style="width: 22px;">
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-down Details-content--hidden">
    <path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path>
</svg>
  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-chevron-right Details-content--shown">
    <path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button>




          <span class="sr-only">
            112 changes: 112 additions &amp; 0 deletions
          </span>
          <span class="diffstat" aria-hidden="true">112 <span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span><span class="diffstat-block-added"></span></span>

        
<span class="Truncate">
  <a title="basic.py" class="Link--primary Truncate-text" href="https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c#diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e">basic.py</a>

  <span data-view-component="true">
  <clipboard-copy data-copy-feedback="Copied!" aria-label="Copy" value="basic.py" data-view-component="true" class="Link--onHover color-fg-muted ml-2 mr-2" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg style="display: none;" aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check color-fg-success">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</clipboard-copy>  <div aria-live="polite" aria-atomic="true" class="sr-only" data-clipboard-copy-feedback=""></div>
</span>
</span>


        
      </div>

      <div class="file-actions pt-0 mb-md-0 mb-2 ml-md-2 flex-shrink-0 flex-md-justify-end">
        <div class="d-flex flex-justify-end">











          

          <details class="js-file-header-dropdown dropdown details-overlay details-reset pr-2 pl-2">
            <summary class="height-full" aria-haspopup="menu" role="button">
              <div class="height-full d-flex flex-items-center Link--secondary">
                <svg aria-label="Show options" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
              </div>
            </summary>
            <details-menu class="dropdown-menu dropdown-menu-sw show-more-popover color-fg-default position-absolute f5" style="width:fit-content; min-width:185px; z-index:99; right: -4px;" role="menu" data-focus-trap="active"><span class="sentinel" tabindex="0" aria-hidden="true"></span>
                            <label role="menuitemradio" class="dropdown-item btn-link text-normal d-block pl-5" tabindex="0" aria-checked="true">
              <span class="position-absolute ml-n4"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg></span>
              <input type="checkbox" checked="" class="d-none js-toggle-file-notes">
              Show comments
            </label>

                            <div role="none" class="dropdown-divider"></div>

                                    <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to make changes.">
      Edit file
    </button>


                                  <button type="button" disabled="" role="menuitem" class="pl-5 dropdown-item btn-link" aria-label="You must be signed in and have push access to delete this file.">
    Delete file
  </button>


                            <div role="none" class="dropdown-divider"></div>

                            <span data-target="copilot-diff-entry.menuItemsSlot"></span>

                
            <span class="sentinel" tabindex="0" aria-hidden="true"></span></details-menu>
          </details>
        </div>
      </div>
    </div>


    <div class="js-file-content Details-content--hidden position-relative" data-hydro-view="{&quot;event_type&quot;:&quot;pull_request.select_diff_range&quot;,&quot;payload&quot;:{&quot;actor_id&quot;:119169570,&quot;pull_request_id&quot;:null,&quot;repository_id&quot;:null,&quot;diff_type&quot;:&quot;UNIFIED&quot;,&quot;whitespace_ignored&quot;:false,&quot;originating_url&quot;:&quot;https://github.com/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c&quot;,&quot;user_id&quot;:119169570}}" data-hydro-view-hmac="875675b4cdb8b35b580ba588a96b3d23126e50555bf282c9c15b095cb80be2a6">


          <div class="data highlight js-blob-wrapper">
            <template class="js-file-alert-template"></template>
<template class="js-line-alert-template"></template>



              
              <table class=" diff-table js-diff-table tab-size  " data-tab-size="8" data-diff-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-paste-markdown-skip="">
                <thead class="sr-only">
                  <tr>
                      <th scope="col">Original file line number</th>
                      <th scope="col">Diff line number</th>
                      <th scope="col">Diff line change</th>
                  </tr>
                </thead>
                <tbody>
                      
      <tr data-position="0">
    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eHL0" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eHR1" class="blob-num blob-num-hunk non-expandable" data-line-number="..."></td>
    <td class="blob-code blob-code-inner blob-code-hunk">@@ -0,0 +1,112 @@</td>
  </tr>

    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR1" data-line-number="1" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="1" data-side="right" data-line="1" data-original-line="+from fastapi import FastAPI
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">from</span> <span class="pl-s1">fastapi</span> <span class="pl-k">import</span> <span class="pl-v">FastAPI</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR2" data-line-number="2" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="2" data-side="right" data-line="2" data-original-line="+import uvicorn
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">import</span> <span class="pl-s1">uvicorn</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR3" data-line-number="3" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="3" data-side="right" data-line="3" data-original-line="+from pydantic import BaseModel
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">from</span> <span class="pl-s1">pydantic</span> <span class="pl-k">import</span> <span class="pl-v">BaseModel</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR4" data-line-number="4" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="4" data-side="right" data-line="4" data-original-line="+from typing import Optional
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">from</span> <span class="pl-s1">typing</span> <span class="pl-k">import</span> <span class="pl-v">Optional</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR5" data-line-number="5" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="5" data-side="right" data-line="5" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR6" data-line-number="6" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="6" data-side="right" data-line="6" data-original-line="+app = FastAPI()
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s1">app</span> <span class="pl-c1">=</span> <span class="pl-v">FastAPI</span>()</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR7" data-line-number="7" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="7" data-side="right" data-line="7" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR8" data-line-number="8" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="8" data-side="right" data-line="8" data-original-line="+news = {
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-s1">news</span> <span class="pl-c1">=</span> {</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR9" data-line-number="9" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="9" data-side="right" data-line="9" data-original-line="+    1:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c1">1</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR10" data-line-number="10" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="10" data-side="right" data-line="10" data-original-line="+    {
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    {</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR11" data-line-number="11" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="11" data-side="right" data-line="11" data-original-line="+        &quot;id&quot;:1,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"id"</span>:<span class="pl-c1">1</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR12" data-line-number="12" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="12" data-side="right" data-line="12" data-original-line="+        &quot;title&quot;: &quot;Top 10 programming language&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"title"</span>: <span class="pl-s">"Top 10 programming language"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR13" data-line-number="13" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="13" data-side="right" data-line="13" data-original-line="+        &quot;content&quot;: &quot;Python is the most popular programming language&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"content"</span>: <span class="pl-s">"Python is the most popular programming language"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR14" data-line-number="14" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="14" data-side="right" data-line="14" data-original-line="+        &quot;author&quot;: &quot;Kalim&quot;
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"author"</span>: <span class="pl-s">"Kalim"</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR15" data-line-number="15" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="15" data-side="right" data-line="15" data-original-line="+    }, 
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    }, </span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR16" data-line-number="16" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="16" data-side="right" data-line="16" data-original-line="+    2:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c1">2</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR17" data-line-number="17" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="17" data-side="right" data-line="17" data-original-line="+    {
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    {</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR18" data-line-number="18" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="18" data-side="right" data-line="18" data-original-line="+        &quot;id&quot;:2,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"id"</span>:<span class="pl-c1">2</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR19" data-line-number="19" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="19" data-side="right" data-line="19" data-original-line="+        &quot;title&quot;: &quot;LLM race in modern era&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"title"</span>: <span class="pl-s">"LLM race in modern era"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR20" data-line-number="20" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="20" data-side="right" data-line="20" data-original-line="+        &quot;content&quot;: &quot;Content on modern LLM models&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"content"</span>: <span class="pl-s">"Content on modern LLM models"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR21" data-line-number="21" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="21" data-side="right" data-line="21" data-original-line="+        &quot;author&quot;: &quot;Ibrahim&quot;
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"author"</span>: <span class="pl-s">"Ibrahim"</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR22" data-line-number="22" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="22" data-side="right" data-line="22" data-original-line="+    }, 
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    }, </span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR23" data-line-number="23" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="23" data-side="right" data-line="23" data-original-line="+    3:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c1">3</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR24" data-line-number="24" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="24" data-side="right" data-line="24" data-original-line="+    {
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    {</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR25" data-line-number="25" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="25" data-side="right" data-line="25" data-original-line="+        &quot;id&quot;:3,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"id"</span>:<span class="pl-c1">3</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR26" data-line-number="26" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="26" data-side="right" data-line="26" data-original-line="+        &quot;title&quot;: &quot;Latest LLM model from Mistral!!! &quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"title"</span>: <span class="pl-s">"Latest LLM model from Mistral!!! "</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR27" data-line-number="27" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="27" data-side="right" data-line="27" data-original-line="+        &quot;content&quot;: &quot;Content on modern LLM models both close &amp; open source&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"content"</span>: <span class="pl-s">"Content on modern LLM models both close &amp; open source"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR28" data-line-number="28" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="28" data-side="right" data-line="28" data-original-line="+        &quot;author&quot;: &quot;Nirjana&quot;
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"author"</span>: <span class="pl-s">"Nirjana"</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR29" data-line-number="29" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="29" data-side="right" data-line="29" data-original-line="+    }, 
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    }, </span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR30" data-line-number="30" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="30" data-side="right" data-line="30" data-original-line="+    4:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-c1">4</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR31" data-line-number="31" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="31" data-side="right" data-line="31" data-original-line="+    {
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    {</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR32" data-line-number="32" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="32" data-side="right" data-line="32" data-original-line="+        &quot;id&quot;:4,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"id"</span>:<span class="pl-c1">4</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR33" data-line-number="33" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="33" data-side="right" data-line="33" data-original-line="+        &quot;title&quot;: &quot;What&#39;s the Google calls on LLM!!!&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"title"</span>: <span class="pl-s">"What's the Google calls on LLM!!!"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR34" data-line-number="34" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="34" data-side="right" data-line="34" data-original-line="+        &quot;content&quot;: &quot;Content on modern LLM models both close &amp; open source&quot;,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"content"</span>: <span class="pl-s">"Content on modern LLM models both close &amp; open source"</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR35" data-line-number="35" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="35" data-side="right" data-line="35" data-original-line="+        &quot;author&quot;: &quot;Kalim&quot;
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"author"</span>: <span class="pl-s">"Kalim"</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR36" data-line-number="36" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="36" data-side="right" data-line="36" data-original-line="+    }
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    }</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR37" data-line-number="37" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="37" data-side="right" data-line="37" data-original-line="+        
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR38" data-line-number="38" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="38" data-side="right" data-line="38" data-original-line="+}
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">}</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR39" data-line-number="39" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="39" data-side="right" data-line="39" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR40" data-line-number="40" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="40" data-side="right" data-line="40" data-original-line="+#pydantic model use korle wrong input dile error dekhabe
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c">#pydantic model use korle wrong input dile error dekhabe</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR41" data-line-number="41" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="41" data-side="right" data-line="41" data-original-line="+class News(BaseModel):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">class</span> <span class="pl-v">News</span>(<span class="pl-v">BaseModel</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR42" data-line-number="42" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="42" data-side="right" data-line="42" data-original-line="+    title: str
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">title</span>: <span class="pl-s1">str</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR43" data-line-number="43" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="43" data-side="right" data-line="43" data-original-line="+    content: str | None = None
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">content</span>: <span class="pl-s1">str</span> <span class="pl-c1">|</span> <span class="pl-c1">None</span> <span class="pl-c1">=</span> <span class="pl-c1">None</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR44" data-line-number="44" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="44" data-side="right" data-line="44" data-original-line="+    author: str
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">author</span>: <span class="pl-s1">str</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR45" data-line-number="45" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="45" data-side="right" data-line="45" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR46" data-line-number="46" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="46" data-side="right" data-line="46" data-original-line="+class UpdateNews(BaseModel):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">class</span> <span class="pl-v">UpdateNews</span>(<span class="pl-v">BaseModel</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR47" data-line-number="47" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="47" data-side="right" data-line="47" data-original-line="+    title: Optional[str] = None
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">title</span>: <span class="pl-v">Optional</span>[<span class="pl-s1">str</span>] <span class="pl-c1">=</span> <span class="pl-c1">None</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR48" data-line-number="48" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="48" data-side="right" data-line="48" data-original-line="+    content: Optional[str] = None
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">content</span>: <span class="pl-v">Optional</span>[<span class="pl-s1">str</span>] <span class="pl-c1">=</span> <span class="pl-c1">None</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR49" data-line-number="49" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="49" data-side="right" data-line="49" data-original-line="+    author: Optional[str] = None
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">author</span>: <span class="pl-v">Optional</span>[<span class="pl-s1">str</span>] <span class="pl-c1">=</span> <span class="pl-c1">None</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR50" data-line-number="50" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="50" data-side="right" data-line="50" data-original-line="+    
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR51" data-line-number="51" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="51" data-side="right" data-line="51" data-original-line="+    
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR52" data-line-number="52" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="52" data-side="right" data-line="52" data-original-line="+#Query parameter(question mark diye jodi kono query korte chai)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c">#Query parameter(question mark diye jodi kono query korte chai)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR53" data-line-number="53" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="53" data-side="right" data-line="53" data-original-line="+@app.get(&quot;/news/{author}&quot;)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">get</span>(<span class="pl-s">"/news/{author}"</span>)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR54" data-line-number="54" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="54" data-side="right" data-line="54" data-original-line="+def get_news_by_author(author: str, title_contains: str = None):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">get_news_by_author</span>(<span class="pl-s1">author</span>: <span class="pl-s1">str</span>, <span class="pl-s1">title_contains</span>: <span class="pl-s1">str</span> <span class="pl-c1">=</span> <span class="pl-c1">None</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR55" data-line-number="55" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="55" data-side="right" data-line="55" data-original-line="+    
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR56" data-line-number="56" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="56" data-side="right" data-line="56" data-original-line="+    filtered_news = [news for news in news.values() if news[&quot;author&quot;].lower()==author.lower()]
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">filtered_news</span> <span class="pl-c1">=</span> [<span class="pl-s1">news</span> <span class="pl-k">for</span> <span class="pl-s1">news</span> <span class="pl-c1">in</span> <span class="pl-s1">news</span>.<span class="pl-en">values</span>() <span class="pl-k">if</span> <span class="pl-s1">news</span>[<span class="pl-s">"author"</span>].<span class="pl-en">lower</span>()<span class="pl-c1">==</span><span class="pl-s1">author</span>.<span class="pl-en">lower</span>()]</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR57" data-line-number="57" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="57" data-side="right" data-line="57" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR58" data-line-number="58" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="58" data-side="right" data-line="58" data-original-line="+    if title_contains:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">title_contains</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR59" data-line-number="59" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="59" data-side="right" data-line="59" data-original-line="+        filtered_news_title = [news for news in filtered_news if title_contains.lower() in news[&quot;title&quot;].lower()]
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s1">filtered_news_title</span> <span class="pl-c1">=</span> [<span class="pl-s1">news</span> <span class="pl-k">for</span> <span class="pl-s1">news</span> <span class="pl-c1">in</span> <span class="pl-s1">filtered_news</span> <span class="pl-k">if</span> <span class="pl-s1">title_contains</span>.<span class="pl-en">lower</span>() <span class="pl-c1">in</span> <span class="pl-s1">news</span>[<span class="pl-s">"title"</span>].<span class="pl-en">lower</span>()]</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR60" data-line-number="60" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="60" data-side="right" data-line="60" data-original-line="+        return filtered_news_title
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-k">return</span> <span class="pl-s1">filtered_news_title</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR61" data-line-number="61" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="61" data-side="right" data-line="61" data-original-line="+    else:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">else</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR62" data-line-number="62" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="62" data-side="right" data-line="62" data-original-line="+        return filtered_news
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-k">return</span> <span class="pl-s1">filtered_news</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR63" data-line-number="63" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="63" data-side="right" data-line="63" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR64" data-line-number="64" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="64" data-side="right" data-line="64" data-original-line="+#normal endpoint to show all news
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c">#normal endpoint to show all news</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR65" data-line-number="65" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="65" data-side="right" data-line="65" data-original-line="+@app.get(&quot;/news&quot;)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">get</span>(<span class="pl-s">"/news"</span>)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR66" data-line-number="66" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="66" data-side="right" data-line="66" data-original-line="+def get_news():
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">get_news</span>():</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR67" data-line-number="67" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="67" data-side="right" data-line="67" data-original-line="+    return news
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">return</span> <span class="pl-s1">news</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR68" data-line-number="68" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="68" data-side="right" data-line="68" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR69" data-line-number="69" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="69" data-side="right" data-line="69" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR70" data-line-number="70" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="70" data-side="right" data-line="70" data-original-line="+#url er moddhe dynamic kono value thakle shetake path parameter bole. (dynamic parameter)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-c">#url er moddhe dynamic kono value thakle shetake path parameter bole. (dynamic parameter)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR71" data-line-number="71" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="71" data-side="right" data-line="71" data-original-line="+@app.get(&quot;/news/{id}&quot;)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">get</span>(<span class="pl-s">"/news/{id}"</span>)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR72" data-line-number="72" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="72" data-side="right" data-line="72" data-original-line="+def get_news_by_id(id: int):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">get_news_by_id</span>(<span class="pl-s1">id</span>: <span class="pl-s1">int</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR73" data-line-number="73" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="73" data-side="right" data-line="73" data-original-line="+    single_news = news.get(id, None)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">single_news</span> <span class="pl-c1">=</span> <span class="pl-s1">news</span>.<span class="pl-en">get</span>(<span class="pl-s1">id</span>, <span class="pl-c1">None</span>)</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR74" data-line-number="74" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="74" data-side="right" data-line="74" data-original-line="+    if single_news:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">single_news</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR75" data-line-number="75" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="75" data-side="right" data-line="75" data-original-line="+        return single_news
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-k">return</span> <span class="pl-s1">single_news</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR76" data-line-number="76" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="76" data-side="right" data-line="76" data-original-line="+    return {&quot;message&quot;: f&quot;News item of id {id} not found&quot;}
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">return</span> {<span class="pl-s">"message"</span>: <span class="pl-s">f"News item of id <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">id</span><span class="pl-kos">}</span></span> not found"</span>}</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR77" data-line-number="77" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="77" data-side="right" data-line="77" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR78" data-line-number="78" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="78" data-side="right" data-line="78" data-original-line="+@app.post(&quot;/create_news&quot;)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">post</span>(<span class="pl-s">"/create_news"</span>)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR79" data-line-number="79" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="79" data-side="right" data-line="79" data-original-line="+def create_news(input_news: News):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">create_news</span>(<span class="pl-s1">input_news</span>: <span class="pl-v">News</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR80" data-line-number="80" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="80" data-side="right" data-line="80" data-original-line="+    id =  max(news.keys())+1
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">id</span> <span class="pl-c1">=</span>  <span class="pl-en">max</span>(<span class="pl-s1">news</span>.<span class="pl-en">keys</span>())<span class="pl-c1">+</span><span class="pl-c1">1</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR81" data-line-number="81" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="81" data-side="right" data-line="81" data-original-line="+    news[id] = {
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">news</span>[<span class="pl-s1">id</span>] <span class="pl-c1">=</span> {</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR82" data-line-number="82" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="82" data-side="right" data-line="82" data-original-line="+        &quot;id&quot;:id,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"id"</span>:<span class="pl-s1">id</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR83" data-line-number="83" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="83" data-side="right" data-line="83" data-original-line="+        &quot;title&quot;: input_news.title,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"title"</span>: <span class="pl-s1">input_news</span>.<span class="pl-s1">title</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR84" data-line-number="84" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="84" data-side="right" data-line="84" data-original-line="+        &quot;content&quot;: input_news.content,
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"content"</span>: <span class="pl-s1">input_news</span>.<span class="pl-s1">content</span>,</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR85" data-line-number="85" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="85" data-side="right" data-line="85" data-original-line="+        &quot;author&quot;: input_news.author
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s">"author"</span>: <span class="pl-s1">input_news</span>.<span class="pl-s1">author</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR86" data-line-number="86" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="86" data-side="right" data-line="86" data-original-line="+    }
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    }</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR87" data-line-number="87" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="87" data-side="right" data-line="87" data-original-line="+    return(news[id])
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">return</span>(<span class="pl-s1">news</span>[<span class="pl-s1">id</span>])</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR88" data-line-number="88" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="88" data-side="right" data-line="88" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR89" data-line-number="89" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="89" data-side="right" data-line="89" data-original-line="+@app.put(&quot;/update_news/{id}&quot;)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">put</span>(<span class="pl-s">"/update_news/{id}"</span>)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR90" data-line-number="90" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="90" data-side="right" data-line="90" data-original-line="+def update_news(id: int, input: UpdateNews):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">update_news</span>(<span class="pl-s1">id</span>: <span class="pl-s1">int</span>, <span class="pl-s1">input</span>: <span class="pl-v">UpdateNews</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR91" data-line-number="91" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="91" data-side="right" data-line="91" data-original-line="+    if id not in news:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">id</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">news</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR92" data-line-number="92" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="92" data-side="right" data-line="92" data-original-line="+        return {&quot;message&quot;: f&quot;News item of id {id} not found&quot;}
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-k">return</span> {<span class="pl-s">"message"</span>: <span class="pl-s">f"News item of id <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">id</span><span class="pl-kos">}</span></span> not found"</span>}</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR93" data-line-number="93" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="93" data-side="right" data-line="93" data-original-line="+    
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR94" data-line-number="94" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="94" data-side="right" data-line="94" data-original-line="+    if input.title is not None:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">input</span>.<span class="pl-s1">title</span> <span class="pl-c1">is</span> <span class="pl-c1">not</span> <span class="pl-c1">None</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR95" data-line-number="95" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="95" data-side="right" data-line="95" data-original-line="+        news[id][&quot;title&quot;] = input.title
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s1">news</span>[<span class="pl-s1">id</span>][<span class="pl-s">"title"</span>] <span class="pl-c1">=</span> <span class="pl-s1">input</span>.<span class="pl-s1">title</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR96" data-line-number="96" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="96" data-side="right" data-line="96" data-original-line="+    if input.content is not None:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">input</span>.<span class="pl-s1">content</span> <span class="pl-c1">is</span> <span class="pl-c1">not</span> <span class="pl-c1">None</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR97" data-line-number="97" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="97" data-side="right" data-line="97" data-original-line="+        news[id][&quot;content&quot;] = input.content
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s1">news</span>[<span class="pl-s1">id</span>][<span class="pl-s">"content"</span>] <span class="pl-c1">=</span> <span class="pl-s1">input</span>.<span class="pl-s1">content</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR98" data-line-number="98" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="98" data-side="right" data-line="98" data-original-line="+    if input.author is not None:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">input</span>.<span class="pl-s1">author</span> <span class="pl-c1">is</span> <span class="pl-c1">not</span> <span class="pl-c1">None</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR99" data-line-number="99" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="99" data-side="right" data-line="99" data-original-line="+        news[id][&quot;author&quot;] = input.author
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-s1">news</span>[<span class="pl-s1">id</span>][<span class="pl-s">"author"</span>] <span class="pl-c1">=</span> <span class="pl-s1">input</span>.<span class="pl-s1">author</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR100" data-line-number="100" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="100" data-side="right" data-line="100" data-original-line="+        
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR101" data-line-number="101" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="101" data-side="right" data-line="101" data-original-line="+    return news[id]
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">return</span> <span class="pl-s1">news</span>[<span class="pl-s1">id</span>]</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR102" data-line-number="102" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="102" data-side="right" data-line="102" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR103" data-line-number="103" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="103" data-side="right" data-line="103" data-original-line="+@app.delete(&quot;/delete_news/{id}&quot;)
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-en">@<span class="pl-s1">app</span>.<span class="pl-en">delete</span>(<span class="pl-s">"/delete_news/{id}"</span>)</span></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR104" data-line-number="104" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="104" data-side="right" data-line="104" data-original-line="+def update_news(id: int):
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">def</span> <span class="pl-en">update_news</span>(<span class="pl-s1">id</span>: <span class="pl-s1">int</span>):</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR105" data-line-number="105" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="105" data-side="right" data-line="105" data-original-line="+    if id not in news:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">if</span> <span class="pl-s1">id</span> <span class="pl-c1">not</span> <span class="pl-c1">in</span> <span class="pl-s1">news</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR106" data-line-number="106" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="106" data-side="right" data-line="106" data-original-line="+        return {&quot;message&quot;: f&quot;News item of id {id} not found&quot;}
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">        <span class="pl-k">return</span> {<span class="pl-s">"message"</span>: <span class="pl-s">f"News item of id <span class="pl-s1"><span class="pl-kos">{</span><span class="pl-s1">id</span><span class="pl-kos">}</span></span> not found"</span>}</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR107" data-line-number="107" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="107" data-side="right" data-line="107" data-original-line="+    
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR108" data-line-number="108" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="108" data-side="right" data-line="108" data-original-line="+    del news[id]
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">del</span> <span class="pl-s1">news</span>[<span class="pl-s1">id</span>]</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR109" data-line-number="109" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="109" data-side="right" data-line="109" data-original-line="+    return {&quot;message&quot;: &quot;News Deleted Successfully&quot;}
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-k">return</span> {<span class="pl-s">"message"</span>: <span class="pl-s">"News Deleted Successfully"</span>}</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR110" data-line-number="110" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="110" data-side="right" data-line="110" data-original-line="+
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><br></span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR111" data-line-number="111" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition  js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="111" data-side="right" data-line="111" data-original-line="+if _name_ == &#39;_main_&#39;:
" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+"><span class="pl-k">if</span> <span class="pl-s1">_name_</span> <span class="pl-c1">==</span> <span class="pl-s">'_main_'</span>:</span></td>
</tr>




    <tr data-hunk="f504186d5635324db4f3d78f19a7c20f96c62c8a66945d36e59d9885dc002011" class="show-top-border">
    <td class="blob-num blob-num-addition empty-cell"></td>

    <td id="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82eR112" data-line-number="112" class="blob-num blob-num-addition js-linkable-line-number js-code-nav-line-number js-blob-rnum"></td>

  <td class="blob-code blob-code-addition js-file-line">
        <button data-path="basic.py" data-anchor="diff-f0e899a4baa61bc78057a745e3e8ef82685eac8c1cbd91434f6a0826e950b82e" data-position="112" data-side="right" data-line="112" data-original-line="+    uvicorn.run(&quot;basic:app&quot;, host=&#39;localhost&#39;, port=8000, reload = True)" aria-label="Add line comment" type="button" data-view-component="true" class="add-line-comment js-add-line-comment js-add-single-line-comment btn-link">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
</button>    <span class="blob-code-inner blob-code-marker js-code-nav-pass " data-code-marker="+">    <span class="pl-s1">uvicorn</span>.<span class="pl-en">run</span>(<span class="pl-s">"basic:app"</span>, <span class="pl-s1">host</span><span class="pl-c1">=</span><span class="pl-s">'localhost'</span>, <span class="pl-s1">port</span><span class="pl-c1">=</span><span class="pl-c1">8000</span>, <span class="pl-s1">reload</span> <span class="pl-c1">=</span> <span class="pl-c1">True</span>)</span>
      <span class="no-nl-marker">
        <svg aria-label="No newline at end of file" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-no-entry">
    <path d="M4.25 7.25a.75.75 0 0 0 0 1.5h7.5a.75.75 0 0 0 0-1.5h-7.5Z"></path><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0Zm-1.5 0a6.5 6.5 0 1 0-13 0 6.5 6.5 0 0 0 13 0Z"></path>
</svg>
      </span>
    </td>
</tr>






                </tbody>
              </table>

          </div>

    </div>
  </div>
</copilot-diff-entry>

  </div>


</div>

<button type="button" class="js-toggle-all-file-notes" data-hotkey="i" style="display:none">Toggle all file notes</button>

<button type="button" class="js-toggle-all-file-annotations" data-hotkey="a" style="display:none">Toggle all file annotations</button>

<svg aria-hidden="true" width="100px" height="84px" viewBox="0 0 340 84" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="diff-placeholder-svg position-absolute bottom-0">
  <defs>
    <clippath id="diff-placeholder">
      <rect x="0" y="0" width="67.0175439" height="11.9298746" rx="2"></rect>
      <rect x="18.9473684" y="47.7194983" width="100.701754" height="11.9298746" rx="2"></rect>
      <rect x="0" y="71.930126" width="37.8947368" height="11.9298746" rx="2"></rect>
      <rect x="127.017544" y="48.0703769" width="53.3333333" height="11.9298746" rx="2"></rect>
      <rect x="187.719298" y="48.0703769" width="72.9824561" height="11.9298746" rx="2"></rect>
      <rect x="76.8421053" y="0" width="140.350877" height="11.9298746" rx="2"></rect>
      <rect x="17.8947368" y="23.8597491" width="140.350877" height="11.9298746" rx="2"></rect>
      <rect x="166.315789" y="23.8597491" width="173.684211" height="11.9298746" rx="2"></rect>
    </clippath>

    <lineargradient id="animated-diff-gradient" x1="0" x2="0" y1="0" y2="1" spreadMethod="reflect">
      <stop offset="0" stop-color="#eee"></stop>
      <stop offset="0.2" stop-color="#eee"></stop>
      <stop offset="0.5" stop-color="#ddd"></stop>
      <stop offset="0.8" stop-color="#eee"></stop>
      <stop offset="1" stop-color="#eee"></stop>
      <animatetransform attributeName="y1" values="0%; 100%; 0" dur="1s" repeatCount="3"></animatetransform>
      <animatetransform attributeName="y2" values="100%; 200%; 0" dur="1s" repeatCount="3"></animatetransform>
    </lineargradient>
  </defs>
</svg>


            <div id="all_commit_comments" class="js-quote-selection-container" data-quote-markdown=".js-comment-body">
  <div class="mb-1 mb-md-3">
    
<div id="partial-visible-comments-header" class="d-flex flex-items-center flex-column-reverse flex-md-row">
  <h3 class="h4 flex-auto text-md-left text-center">
    0 comments
    on commit <code class="commit-sha">c653b67</code>
  </h3>

  <div class="flex-shrink-0 mb-2 mb-md-0">
    
  </div>
</div>

  </div>

  <div id="comments" class="comment-holder ml-0 pl-0 ml-md-6 pl-md-3">
    

  <!-- Rendered timeline since 2024-08-19 07:15:00 -->
  <div id="partial-timeline-marker" class="js-timeline-marker js-socket-channel js-updatable-content" data-channel="eyJjIjoicmVwbzo4NDQ1NjQxOTA6Y29tbWl0OmM2NTNiNjc3OWYzYjlkOGYwZTgyNDI4ZDQ1YjY2NWNlZWU1NGE2OGMiLCJ0IjoxNzI1MTM1NTIzfQ==--0bdd33059b72ef23f756986f62bb743448ea9a86101b6ac3609732fe7b677643" data-url="/NTNirjana/session-2--fastapi/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c/show_partial?partial=commit%2Ftimeline_marker&amp;since=1724076900" data-last-modified="Mon, 19 Aug 2024 14:15:00 GMT">

  </div>

  </div>

  

  
  <div class="js-comment-container ml-0 pl-0 ml-md-6 pl-md-3">
    <div class="d-none d-md-block">
      <span class="timeline-comment-avatar "><a class="d-inline-block" data-hovercard-type="user" data-hovercard-url="/users/c193249Tasnia/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="https://github.com/c193249Tasnia"><img class="avatar avatar-user" src="https://avatars.githubusercontent.com/u/119169570?s=80&amp;v=4" width="40" height="40" alt="@c193249Tasnia"></a></span>
    </div>

    <!-- '"` --><!-- </textarea></xmp> --><form class="js-new-comment-form js-needs-timeline-marker-header" data-turbo="false" action="https://github.com/NTNirjana/session-2--fastapi/commit_comment/create" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="nuI7jjVGpNmtm_i4C4NGuqfxxQWRWSyG0fEW6Nd5ubbet4luwljE0EMp6EnY1b2edVLhccX5gL5MYJVdQTCwhg">
      <input type="text" name="required_field_076b" hidden="hidden" class="form-control"><input type="hidden" name="timestamp" value="1725135523447" autocomplete="off" class="form-control"><input type="hidden" name="timestamp_secret" value="bedc673bde593706bbafa22ca7819a686fb57241774adf16864c089519be9527" autocomplete="off" class="form-control">
      <div>
          <input type="hidden" name="commit_id" value="c653b6779f3b9d8f0e82428d45b665ceee54a68c">
          <input type="hidden" name="path" value="">
            

<label for="new_commit_comment_field" data-view-component="true" class="sr-only position-absolute">Comment</label>
<tab-container class="js-previewable-comment-form write-selected Box CommentBox" data-preview-url="/preview?markdown_unsupported=false&amp;repository=844564190&amp;subject=c653b6779f3b9d8f0e82428d45b665ceee54a68c&amp;subject_type=Commit">
  <input type="hidden" value="uhS5Q2wtMmQ0gpHN-FWnLtz7Rx4SL0206TCLZKUAxIhnfyAle-nY2gUVvo8s2OTTJ_Am0XF06CRwv2uEkNUXEQ" data-csrf="true" class="js-data-preview-url-csrf">
  <div class="tabnav CommentBox-header width-full">
      <div class="tabnav-tabs" role="tablist" aria-label="Add a comment">
        <button type="button" class="btn-link tabnav-tab write-tab js-write-tab" role="tab" id="write_tab_previewable-comment-form-component-21d5c885-1a44-447f-be27-dd80e88c4d59" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;WRITE_TAB&quot;,&quot;label&quot;:null}" aria-selected="true" tabindex="0">
          Write
        </button>
        <button type="button" class="btn-link tabnav-tab preview-tab js-preview-tab" role="tab" id="preview_tab_previewable-comment-form-component-21d5c885-1a44-447f-be27-dd80e88c4d59" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;PREVIEW_TAB&quot;,&quot;label&quot;:null}" aria-selected="false" tabindex="-1">
          Preview
        </button>
      </div>
    <markdown-toolbar role="presentation" for="new_commit_comment_field" data-no-focus="true" data-view-component="true" class="CommentBox-toolbar">
  <action-bar role="toolbar" data-view-component="true" class="ActionBar" data-catalyst="" style="overflow: visible;">
  <div data-target="action-bar.itemContainer" data-view-component="true" class="ActionBar-item-container">
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-e456534a-3b1f-4234-af00-32f767be96a2" data-md-button="header-3" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;HEADING&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-de301156-a042-4180-a255-0535a600c82c" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="0">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heading Button-visual">
    <path d="M3.75 2a.75.75 0 0 1 .75.75V7h7V2.75a.75.75 0 0 1 1.5 0v10.5a.75.75 0 0 1-1.5 0V8.5h-7v4.75a.75.75 0 0 1-1.5 0V2.75A.75.75 0 0 1 3.75 2Z"></path>
</svg>
</button><tool-tip id="tooltip-de301156-a042-4180-a255-0535a600c82c" for="action-bar-e456534a-3b1f-4234-af00-32f767be96a2" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Heading</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-cebfa1ce-80fc-466e-acb4-30378dba45c3" data-md-button="bold" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+b" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;BOLD&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-19888f06-efbb-40f2-9772-78640676e1d7" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bold Button-visual">
    <path d="M4 2h4.5a3.501 3.501 0 0 1 2.852 5.53A3.499 3.499 0 0 1 9.5 14H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm1 7v3h4.5a1.5 1.5 0 0 0 0-3Zm3.5-2a1.5 1.5 0 0 0 0-3H5v3Z"></path>
</svg>
</button><tool-tip id="tooltip-19888f06-efbb-40f2-9772-78640676e1d7" for="action-bar-cebfa1ce-80fc-466e-acb4-30378dba45c3" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Bold</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-6076fe24-0ce6-4062-9c73-574573684cd2" data-md-button="italic" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+i" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;ITALIC&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-e2d644e7-0fe0-4e06-86e0-fb93a61f54a9" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-italic Button-visual">
    <path d="M6 2.75A.75.75 0 0 1 6.75 2h6.5a.75.75 0 0 1 0 1.5h-2.505l-3.858 9H9.25a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.505l3.858-9H6.75A.75.75 0 0 1 6 2.75Z"></path>
</svg>
</button><tool-tip id="tooltip-e2d644e7-0fe0-4e06-86e0-fb93a61f54a9" for="action-bar-6076fe24-0ce6-4062-9c73-574573684cd2" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Italic</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-47cc213e-2560-4a1e-a702-b03897518643" data-md-button="quote" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+&gt;" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;QUOTE&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-31ae68d3-c866-440f-8375-ac06c1b8cfac" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-quote Button-visual">
    <path d="M1.75 2.5h10.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Zm4 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2.5 7.75v6a.75.75 0 0 1-1.5 0v-6a.75.75 0 0 1 1.5 0Z"></path>
</svg>
</button><tool-tip id="tooltip-31ae68d3-c866-440f-8375-ac06c1b8cfac" for="action-bar-47cc213e-2560-4a1e-a702-b03897518643" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Quote</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-938cac08-1f3d-44d0-8ed0-e0198f76041a" data-md-button="code" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+e" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;CODE&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-76c9286d-4f47-4780-be70-643268fb6909" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code Button-visual">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
</button><tool-tip id="tooltip-76c9286d-4f47-4780-be70-643268fb6909" for="action-bar-938cac08-1f3d-44d0-8ed0-e0198f76041a" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Code</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-c1046ec7-ea36-4b22-ba69-ca924372d99c" data-md-button="link" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+k" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;LINK&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-60425813-401c-4ce3-b16f-13bc7091dc43" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link Button-visual">
    <path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path>
</svg>
</button><tool-tip id="tooltip-60425813-401c-4ce3-b16f-13bc7091dc43" for="action-bar-c1046ec7-ea36-4b22-ba69-ca924372d99c" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Link</tool-tip>
</div>
      <hr role="presentation" aria-hidden="true" data-targets="action-bar.items" data-view-component="true" class="ActionBar-item ActionBar-divider" data-offset-width="16.66666668653488" style="visibility: visible;">
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-96581ad3-febc-4501-a046-3ca22e84d8c5" data-md-button="ordered-list" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+&amp;" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;ORDERED_LIST&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-4375ad29-9da3-4f8e-91ef-095a1cbddb59" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-ordered Button-visual">
    <path d="M5 3.25a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 3.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 8.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1-.75-.75ZM.924 10.32a.5.5 0 0 1-.851-.525l.001-.001.001-.002.002-.004.007-.011c.097-.144.215-.273.348-.384.228-.19.588-.392 1.068-.392.468 0 .858.181 1.126.484.259.294.377.673.377 1.038 0 .987-.686 1.495-1.156 1.845l-.047.035c-.303.225-.522.4-.654.597h1.357a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5c0-1.005.692-1.52 1.167-1.875l.035-.025c.531-.396.8-.625.8-1.078a.57.57 0 0 0-.128-.376C1.806 10.068 1.695 10 1.5 10a.658.658 0 0 0-.429.163.835.835 0 0 0-.144.153ZM2.003 2.5V6h.503a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1h.503V3.308l-.28.14a.5.5 0 0 1-.446-.895l1.003-.5a.5.5 0 0 1 .723.447Z"></path>
</svg>
</button><tool-tip id="tooltip-4375ad29-9da3-4f8e-91ef-095a1cbddb59" for="action-bar-96581ad3-febc-4501-a046-3ca22e84d8c5" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Numbered list</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-d7ed7773-b9f8-4a2c-bd71-ecee40bdcd49" data-md-button="unordered-list" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+*" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;UNORDERED_LIST&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-4822db27-8972-4ce2-b300-fdb82aa9d16d" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered Button-visual">
    <path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
</button><tool-tip id="tooltip-4822db27-8972-4ce2-b300-fdb82aa9d16d" for="action-bar-d7ed7773-b9f8-4a2c-bd71-ecee40bdcd49" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Unordered list</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-0e1e99ef-e0ac-4708-b188-9d14adf150c1" data-md-button="task-list" data-hotkey-scope="new_commit_comment_field" data-hotkey="Control+Shift+L" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;TASK_LIST&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-00c3ae5e-c003-4388-ba0e-ae2d92671ba5" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tasklist Button-visual">
    <path d="M2 2h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm4.655 8.595a.75.75 0 0 1 0 1.06L4.03 14.28a.75.75 0 0 1-1.06 0l-1.5-1.5a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l.97.97 2.095-2.095a.75.75 0 0 1 1.06 0ZM9.75 2.5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm-7.25-9v3h3v-3Z"></path>
</svg>
</button><tool-tip id="tooltip-00c3ae5e-c003-4388-ba0e-ae2d92671ba5" for="action-bar-0e1e99ef-e0ac-4708-b188-9d14adf150c1" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Task list</tool-tip>
</div>
      <hr role="presentation" aria-hidden="true" data-targets="action-bar.items" data-view-component="true" class="ActionBar-item ActionBar-divider" data-offset-width="16.66666668653488" style="visibility: visible;">
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-d36e6939-a9e6-47b2-8d8e-dfa1abe40412" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;ATTACH_FILES&quot;,&quot;label&quot;:null}" data-file-attachment-for="fc-new_commit_comment_field" aria-labelledby="tooltip-d5f07851-0549-4ac7-b8f5-5488c2488730" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-paperclip Button-visual">
    <path d="M12.212 3.02a1.753 1.753 0 0 0-2.478.003l-5.83 5.83a3.007 3.007 0 0 0-.88 2.127c0 .795.315 1.551.88 2.116.567.567 1.333.89 2.126.89.79 0 1.548-.321 2.116-.89l5.48-5.48a.75.75 0 0 1 1.061 1.06l-5.48 5.48a4.492 4.492 0 0 1-3.177 1.33c-1.2 0-2.345-.487-3.187-1.33a4.483 4.483 0 0 1-1.32-3.177c0-1.195.475-2.341 1.32-3.186l5.83-5.83a3.25 3.25 0 0 1 5.553 2.297c0 .863-.343 1.691-.953 2.301L7.439 12.39c-.375.377-.884.59-1.416.593a1.998 1.998 0 0 1-1.412-.593 1.992 1.992 0 0 1 0-2.828l5.48-5.48a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-5.48 5.48a.492.492 0 0 0 0 .707.499.499 0 0 0 .352.154.51.51 0 0 0 .356-.154l5.833-5.827a1.755 1.755 0 0 0 0-2.481Z"></path>
</svg>
</button><tool-tip id="tooltip-d5f07851-0549-4ac7-b8f5-5488c2488730" for="action-bar-d36e6939-a9e6-47b2-8d8e-dfa1abe40412" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Attach files</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-2263b0be-2aac-4865-8fc0-4b1687a6031f" data-md-button="mention" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;MENTION&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-504354fb-a2d8-4a71-a613-ac1e4232882a" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-mention Button-visual">
    <path d="M4.75 2.37a6.501 6.501 0 0 0 6.5 11.26.75.75 0 0 1 .75 1.298A7.999 7.999 0 0 1 .989 4.148 8 8 0 0 1 16 7.75v1.5a2.75 2.75 0 0 1-5.072 1.475 3.999 3.999 0 0 1-6.65-4.19A4 4 0 0 1 12 8v1.25a1.25 1.25 0 0 0 2.5 0V7.867a6.5 6.5 0 0 0-9.75-5.496ZM10.5 8a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
</button><tool-tip id="tooltip-504354fb-a2d8-4a71-a613-ac1e4232882a" for="action-bar-2263b0be-2aac-4865-8fc0-4b1687a6031f" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Mention</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-fb2e3877-f7ed-48ca-b08f-01b391b43f74" data-md-button="ref" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;REFERENCE&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-63766724-b0ef-489a-b771-ebd98b8d9000" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-cross-reference Button-visual">
    <path d="M2.75 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h4.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 13H9.06l-2.573 2.573A1.458 1.458 0 0 1 4 14.543V13H2.75A1.75 1.75 0 0 1 1 11.25v-7.5C1 2.784 1.784 2 2.75 2h5.5a.75.75 0 0 1 0 1.5ZM16 1.25v4.146a.25.25 0 0 1-.427.177L14.03 4.03l-3.75 3.75a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l3.75-3.75-1.543-1.543A.25.25 0 0 1 11.604 1h4.146a.25.25 0 0 1 .25.25Z"></path>
</svg>
</button><tool-tip id="tooltip-63766724-b0ef-489a-b771-ebd98b8d9000" for="action-bar-fb2e3877-f7ed-48ca-b08f-01b391b43f74" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Reference</tool-tip>
</div>
      <div data-targets="action-bar.items" data-view-component="true" class="ActionBar-item" data-offset-width="32" style="visibility: visible;"><button id="action-bar-78c33199-63d1-4799-9d84-4ac3c33f5961" data-show-dialog-id="saved_replies_menu_new_commit_comment_field-dialog" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;SAVED_REPLIES&quot;,&quot;label&quot;:null}" aria-labelledby="tooltip-b7fd54f3-0f56-486e-81b5-307b05f0d80e" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium" tabindex="-1">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-reply Button-visual">
    <path d="M6.78 1.97a.75.75 0 0 1 0 1.06L3.81 6h6.44A4.75 4.75 0 0 1 15 10.75v2.5a.75.75 0 0 1-1.5 0v-2.5a3.25 3.25 0 0 0-3.25-3.25H3.81l2.97 2.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L1.47 7.28a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0Z"></path>
</svg>
</button><tool-tip id="tooltip-b7fd54f3-0f56-486e-81b5-307b05f0d80e" for="action-bar-78c33199-63d1-4799-9d84-4ac3c33f5961" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Saved replies</tool-tip>
</div>
</div>    <action-menu data-target="action-bar.moreMenu" hidden="" data-select-variant="none" data-view-component="true" class="ActionBar-more-menu" data-catalyst="">
  <focus-group direction="vertical" mnemonics="" retain="">
    <button id="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-button" popovertarget="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-overlay" aria-controls="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-list" aria-haspopup="true" aria-labelledby="tooltip-5d296462-c427-4e8e-9496-5286c547f734" type="button" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium">  <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-kebab-horizontal Button-visual">
    <path d="M8 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Zm13 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z"></path>
</svg>
</button><tool-tip id="tooltip-5d296462-c427-4e8e-9496-5286c547f734" for="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-button" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute" aria-hidden="true" role="tooltip"><template shadowrootmode="open"><style>
      :host {
        --tooltip-top: var(--tool-tip-position-top, 0);
        --tooltip-left: var(--tool-tip-position-left, 0);
        padding: var(--overlay-paddingBlock-condensed) var(--overlay-padding-condensed) !important;
        font: var(--text-body-shorthand-small);
        color: var(--tooltip-fgColor, var(--fgColor-onEmphasis)) !important;
        text-align: center;
        text-decoration: none;
        text-shadow: none;
        text-transform: none;
        letter-spacing: normal;
        word-wrap: break-word;
        white-space: pre;
        background: var(--tooltip-bgColor, var(--bgColor-emphasis)) !important;
        border-radius: var(--borderRadius-medium);
        border: 0 !important;
        opacity: 0;
        max-width: var(--overlay-width-small);
        word-wrap: break-word;
        white-space: normal;
        width: max-content !important;
        inset: var(--tooltip-top) auto auto var(--tooltip-left) !important;
        overflow: visible !important;
        text-wrap: balance;
      }

      :host(:is(.tooltip-n, .tooltip-nw, .tooltip-ne)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) - var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(:is(.tooltip-s, .tooltip-sw, .tooltip-se)) {
        --tooltip-top: calc(var(--tool-tip-position-top, 0) + var(--overlay-offset, 0.25rem));
        --tooltip-left: var(--tool-tip-position-left);
      }

      :host(.tooltip-w) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) - var(--overlay-offset, 0.25rem));
      }

      :host(.tooltip-e) {
        --tooltip-top: var(--tool-tip-position-top);
        --tooltip-left: calc(var(--tool-tip-position-left, 0) + var(--overlay-offset, 0.25rem));
      }

      :host:after{
        position: absolute;
        display: block;
        right: 0;
        left: 0;
        height: var(--overlay-offset, 0.25rem);
        content: "";
      }

      :host(.tooltip-s):after,
      :host(.tooltip-se):after,
      :host(.tooltip-sw):after {
        bottom: 100%
      }

      :host(.tooltip-n):after,
      :host(.tooltip-ne):after,
      :host(.tooltip-nw):after {
        top: 100%;
      }

      @keyframes tooltip-appear {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      :host(:popover-open),
      :host(:popover-open):before {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      :host(.\:popover-open) {
        animation-name: tooltip-appear;
        animation-duration: .1s;
        animation-fill-mode: forwards;
        animation-timing-function: ease-in;
      }

      @media (forced-colors: active) {
        :host {
          outline: solid 1px transparent;
        }

        :host:before {
          display: none;
        }
      }
    </style><slot></slot></template>Menu</tool-tip>


<anchored-position id="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-overlay" anchor="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-button" align="end" side="outside-bottom" anchor-offset="normal" popover="auto" data-view-component="true" style="inset: 0px auto auto 0px;">
  <div data-view-component="true" class="Overlay Overlay--size-auto">
    
      <div data-view-component="true" class="Overlay-body Overlay-body--paddingNone">          <action-list data-catalyst="">
  <div data-view-component="true">
    <ul aria-labelledby="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-button" id="action-bar-0ad05dec-23d6-45ac-8c91-a548a7e966c4-list" role="menu" data-view-component="true" class="ActionListWrap--inset ActionListWrap">
        <li value="" hidden="" data-for="action-bar-e456534a-3b1f-4234-af00-32f767be96a2" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-fc7e6d3a-cd08-4931-b233-27470a3dafc0" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-heading">
    <path d="M3.75 2a.75.75 0 0 1 .75.75V7h7V2.75a.75.75 0 0 1 1.5 0v10.5a.75.75 0 0 1-1.5 0V8.5h-7v4.75a.75.75 0 0 1-1.5 0V2.75A.75.75 0 0 1 3.75 2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Heading
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-cebfa1ce-80fc-466e-acb4-30378dba45c3" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-48e652b1-eb14-4801-91ac-4a8231505d6e" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bold">
    <path d="M4 2h4.5a3.501 3.501 0 0 1 2.852 5.53A3.499 3.499 0 0 1 9.5 14H4a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm1 7v3h4.5a1.5 1.5 0 0 0 0-3Zm3.5-2a1.5 1.5 0 0 0 0-3H5v3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Bold
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-6076fe24-0ce6-4062-9c73-574573684cd2" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-29d25d3d-95d3-4fe7-bde4-387567e5c514" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-italic">
    <path d="M6 2.75A.75.75 0 0 1 6.75 2h6.5a.75.75 0 0 1 0 1.5h-2.505l-3.858 9H9.25a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1 0-1.5h2.505l3.858-9H6.75A.75.75 0 0 1 6 2.75Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Italic
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-47cc213e-2560-4a1e-a702-b03897518643" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-b0feb856-166b-45fb-bb68-7c2e2113ede9" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-quote">
    <path d="M1.75 2.5h10.5a.75.75 0 0 1 0 1.5H1.75a.75.75 0 0 1 0-1.5Zm4 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2.5 7.75v6a.75.75 0 0 1-1.5 0v-6a.75.75 0 0 1 1.5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Quote
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-938cac08-1f3d-44d0-8ed0-e0198f76041a" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-73845b25-c8c3-44bf-a5b2-b49c9a2f3cd6" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-code">
    <path d="m11.28 3.22 4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734L13.94 8l-3.72-3.72a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215Zm-6.56 0a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042L2.06 8l3.72 3.72a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L.47 8.53a.75.75 0 0 1 0-1.06Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Code
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-c1046ec7-ea36-4b22-ba69-ca924372d99c" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-14023358-1feb-4fe2-9aa8-924dd2c65439" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-link">
    <path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Link
</span>      
</button>
  
</li>
        <li hidden="" role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        <li value="" hidden="" data-for="action-bar-96581ad3-febc-4501-a046-3ca22e84d8c5" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-3a6fd55a-c73a-400b-9f44-c3627e011faf" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-ordered">
    <path d="M5 3.25a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 3.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5A.75.75 0 0 1 5 8.25Zm0 5a.75.75 0 0 1 .75-.75h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1-.75-.75ZM.924 10.32a.5.5 0 0 1-.851-.525l.001-.001.001-.002.002-.004.007-.011c.097-.144.215-.273.348-.384.228-.19.588-.392 1.068-.392.468 0 .858.181 1.126.484.259.294.377.673.377 1.038 0 .987-.686 1.495-1.156 1.845l-.047.035c-.303.225-.522.4-.654.597h1.357a.5.5 0 0 1 0 1H.5a.5.5 0 0 1-.5-.5c0-1.005.692-1.52 1.167-1.875l.035-.025c.531-.396.8-.625.8-1.078a.57.57 0 0 0-.128-.376C1.806 10.068 1.695 10 1.5 10a.658.658 0 0 0-.429.163.835.835 0 0 0-.144.153ZM2.003 2.5V6h.503a.5.5 0 0 1 0 1H.5a.5.5 0 0 1 0-1h.503V3.308l-.28.14a.5.5 0 0 1-.446-.895l1.003-.5a.5.5 0 0 1 .723.447Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Numbered list
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-d7ed7773-b9f8-4a2c-bd71-ecee40bdcd49" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-faf896d7-f286-4339-98c6-53395eb65954" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-list-unordered">
    <path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Unordered list
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-0e1e99ef-e0ac-4708-b188-9d14adf150c1" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-5aec093c-0e5d-4405-8d92-b4a2204f8d9e" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-tasklist">
    <path d="M2 2h4a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1Zm4.655 8.595a.75.75 0 0 1 0 1.06L4.03 14.28a.75.75 0 0 1-1.06 0l-1.5-1.5a.749.749 0 0 1 .326-1.275.749.749 0 0 1 .734.215l.97.97 2.095-2.095a.75.75 0 0 1 1.06 0ZM9.75 2.5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm0 5h5.5a.75.75 0 0 1 0 1.5h-5.5a.75.75 0 0 1 0-1.5Zm-7.25-9v3h3v-3Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Task list
</span>      
</button>
  
</li>
        <li hidden="" role="presentation" aria-hidden="true" data-view-component="true" class="ActionList-sectionDivider"></li>
        <li value="" hidden="" data-for="action-bar-d36e6939-a9e6-47b2-8d8e-dfa1abe40412" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-b5d69964-baf5-4a86-9824-ef6fad6d0a17" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-paperclip">
    <path d="M12.212 3.02a1.753 1.753 0 0 0-2.478.003l-5.83 5.83a3.007 3.007 0 0 0-.88 2.127c0 .795.315 1.551.88 2.116.567.567 1.333.89 2.126.89.79 0 1.548-.321 2.116-.89l5.48-5.48a.75.75 0 0 1 1.061 1.06l-5.48 5.48a4.492 4.492 0 0 1-3.177 1.33c-1.2 0-2.345-.487-3.187-1.33a4.483 4.483 0 0 1-1.32-3.177c0-1.195.475-2.341 1.32-3.186l5.83-5.83a3.25 3.25 0 0 1 5.553 2.297c0 .863-.343 1.691-.953 2.301L7.439 12.39c-.375.377-.884.59-1.416.593a1.998 1.998 0 0 1-1.412-.593 1.992 1.992 0 0 1 0-2.828l5.48-5.48a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-5.48 5.48a.492.492 0 0 0 0 .707.499.499 0 0 0 .352.154.51.51 0 0 0 .356-.154l5.833-5.827a1.755 1.755 0 0 0 0-2.481Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Attach files
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-2263b0be-2aac-4865-8fc0-4b1687a6031f" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-30031a93-6a0a-4cc4-b326-2dffe2d64c5f" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-mention">
    <path d="M4.75 2.37a6.501 6.501 0 0 0 6.5 11.26.75.75 0 0 1 .75 1.298A7.999 7.999 0 0 1 .989 4.148 8 8 0 0 1 16 7.75v1.5a2.75 2.75 0 0 1-5.072 1.475 3.999 3.999 0 0 1-6.65-4.19A4 4 0 0 1 12 8v1.25a1.25 1.25 0 0 0 2.5 0V7.867a6.5 6.5 0 0 0-9.75-5.496ZM10.5 8a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Mention
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-fb2e3877-f7ed-48ca-b08f-01b391b43f74" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-84760501-62c7-4d35-84db-b878ce86da8d" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-cross-reference">
    <path d="M2.75 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h4.5a.25.25 0 0 0 .25-.25v-2.5a.75.75 0 0 1 1.5 0v2.5A1.75 1.75 0 0 1 13.25 13H9.06l-2.573 2.573A1.458 1.458 0 0 1 4 14.543V13H2.75A1.75 1.75 0 0 1 1 11.25v-7.5C1 2.784 1.784 2 2.75 2h5.5a.75.75 0 0 1 0 1.5ZM16 1.25v4.146a.25.25 0 0 1-.427.177L14.03 4.03l-3.75 3.75a.749.749 0 0 1-1.275-.326.749.749 0 0 1 .215-.734l3.75-3.75-1.543-1.543A.25.25 0 0 1 11.604 1h4.146a.25.25 0 0 1 .25.25Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Reference
</span>      
</button>
  
</li>
        <li value="" hidden="" data-for="action-bar-78c33199-63d1-4799-9d84-4ac3c33f5961" data-action="click:action-bar#menuItemClick" data-targets="action-list.items" role="none" data-view-component="true" class="ActionListItem">
    
    
    <button tabindex="-1" id="item-05949dea-86fd-404a-ad49-0a05029822e2" type="button" role="menuitem" data-view-component="true" class="ActionListContent ActionListContent--visual16">
        <span class="ActionListItem-visual ActionListItem-visual--leading">
          <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-reply">
    <path d="M6.78 1.97a.75.75 0 0 1 0 1.06L3.81 6h6.44A4.75 4.75 0 0 1 15 10.75v2.5a.75.75 0 0 1-1.5 0v-2.5a3.25 3.25 0 0 0-3.25-3.25H3.81l2.97 2.97a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L1.47 7.28a.75.75 0 0 1 0-1.06l4.25-4.25a.75.75 0 0 1 1.06 0Z"></path>
</svg>
        </span>
      
        <span data-view-component="true" class="ActionListItem-label">
          Saved replies
</span>      
</button>
  
</li>
</ul>    
</div></action-list>


</div>
      
</div></anchored-position>  </focus-group>
</action-menu></action-bar></markdown-toolbar>

<dialog-helper>
  <dialog id="saved_replies_menu_new_commit_comment_field-dialog" aria-modal="true" aria-labelledby="saved_replies_menu_new_commit_comment_field-dialog-title" aria-describedby="saved_replies_menu_new_commit_comment_field-dialog-description" data-view-component="true" class="Overlay Overlay-whenNarrow Overlay--size-medium Overlay--motion-scaleFade Overlay--placement-bottom-whenNarrow js-saved-reply-container">
    <div data-view-component="true" class="Overlay-header">
  <div class="Overlay-headerContentWrap">
    <div class="Overlay-titleWrap">
      <h1 class="Overlay-title " id="saved_replies_menu_new_commit_comment_field-dialog-title">
        Select a reply
      </h1>
        
    </div>
    <div class="Overlay-actionWrap">
      <button data-close-dialog-id="saved_replies_menu_new_commit_comment_field-dialog" aria-label="Close" type="button" data-view-component="true" class="close-button Overlay-closeButton"><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg></button>
    </div>
  </div>
  
</div>
      <scrollable-region data-labelled-by="saved_replies_menu_new_commit_comment_field-dialog-title" data-catalyst="" style="overflow: auto;">
        <div data-view-component="true" class="Overlay-body">    <include-fragment class="js-saved-reply-include-fragment" role="menuitem" aria-label="Loading" src="/settings/replies?context=none" loading="lazy"><template shadowrootmode="open"><style>:host {display: block;}</style><slot></slot></template>
      <svg style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" aria-hidden="true" data-view-component="true" class="my-6 mx-auto d-block anim-rotate">
  <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
  <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
</svg>  <span class="spinner-screenreader-text sr-only">Loading</span>

    </include-fragment>
</div>
      </scrollable-region>
      <div data-view-component="true" class="Overlay-footer Overlay-footer--alignEnd Overlay-footer--divided">    <a href="https://github.com/settings/replies?return_to=1" data-view-component="true" class="Button--invisible Button--medium Button Button--fullWidth">  <span class="Button-content Button-content--alignStart">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-plus">
    <path d="M7.75 2a.75.75 0 0 1 .75.75V7h4.25a.75.75 0 0 1 0 1.5H8.5v4.25a.75.75 0 0 1-1.5 0V8.5H2.75a.75.75 0 0 1 0-1.5H7V2.75A.75.75 0 0 1 7.75 2Z"></path>
</svg>
      </span>
    <span class="Button-label">Create a new saved reply</span>
  </span>
</a>
</div>
</dialog></dialog-helper>


  </div>

  <div class="comment-form-error js-comment-form-error" role="alert" hidden="">
    There was an error creating your Commit.
  </div>

  <file-attachment class="js-upload-markdown-image is-default" input="fc-new_commit_comment_field" role="tabpanel" aria-labelledby="write_tab_previewable-comment-form-component-21d5c885-1a44-447f-be27-dd80e88c4d59" data-tab-container-no-tabstop="true" data-upload-repository-id="844564190" data-upload-policy-url="/upload/policies/assets"><input type="hidden" value="pRUz6fiQ6wJk04hr_vYxXwN5O2wO8m1fOdrJaBBb4N5KoifKHWtJkga491ip4QoJAIQUa987w-JaGDQzaC48EQ" data-csrf="true" class="js-data-upload-policy-url-csrf">
    <div class="js-write-bucket position-relative">
        <input type="hidden" name="saved_reply_id" id="new_commit_comment_field_saved_reply_id" class="js-resettable-field" value="" data-reset-value="">

      <text-expander keys=": @ #" data-issue-url="/suggestions/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c?issue_suggester=1&amp;repository=session-2--fastapi&amp;user_id=NTNirjana" data-mention-url="/suggestions/commit/c653b6779f3b9d8f0e82428d45b665ceee54a68c?mention_suggester=1&amp;repository=session-2--fastapi&amp;user_id=NTNirjana" multiword="#" data-emoji-url="/autocomplete/emoji">
          
        <div class="CommentBox-container">
          <textarea name="comment[body]" id="new_commit_comment_field" placeholder=" " data-required-trimmed="Text field is empty" class="js-comment-field js-paste-markdown js-task-list-field js-quick-submit FormControl-textarea CommentBox-input js-size-to-fit js-session-resumable js-saved-reply-shortcut-comment-field" dir="auto" aria-describedby="placeholder_previewable-comment-form-component-21d5c885-1a44-447f-be27-dd80e88c4d59" required=""></textarea>
          <p class="CommentBox-placeholder" id="placeholder_previewable-comment-form-component-21d5c885-1a44-447f-be27-dd80e88c4d59" data-comment-box-placeholder="" aria-hidden="true">
            Leave a comment
          </p>
        </div>

      </text-expander>
        <input accept=".gif,.jpeg,.jpg,.mov,.mp4,.png,.svg,.webm,.cpuprofile,.csv,.dmp,.docx,.fodg,.fodp,.fods,.fodt,.gz,.json,.jsonc,.log,.md,.odf,.odg,.odp,.ods,.odt,.patch,.pdf,.pptx,.tgz,.txt,.xls,.xlsx,.zip" type="file" multiple="" hidden="" id="fc-new_commit_comment_field">
        <div class="file-attachment-errors">
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 bad-file repository-required Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">We don’t support that file type.</p>
        <p>Try again with GIF, JPEG, JPG, MOV, MP4, PNG, SVG, WEBM, CPUPROFILE, CSV, DMP, DOCX, FODG, FODP, FODS, FODT, GZ, JSON, JSONC, LOG, MD, ODF, ODG, ODP, ODS, ODT, PATCH, PDF, PPTX, TGZ, TXT, XLS, XLSX or ZIP.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 bad-permissions Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">Attaching documents requires write permission to this repository.</p>
        <p>Try again with GIF, JPEG, JPG, MOV, MP4, PNG, SVG, WEBM, CPUPROFILE, CSV, DMP, DOCX, FODG, FODP, FODS, FODT, GZ, JSON, JSONC, LOG, MD, ODF, ODG, ODP, ODS, ODT, PATCH, PDF, PPTX, TGZ, TXT, XLS, XLSX or ZIP.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 too-big js-upload-too-big Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText"></p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 empty Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">This file is empty.</p>
        <p>Try again with a file that’s not empty.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 hidden-file Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">This file is hidden.</p>
        <p>Try again with another file.</p>
</div></div></x-banner>
          <x-banner data-dismiss-scheme="none" data-view-component="true" data-catalyst="">
  <div data-view-component="true" class="rounded-bottom-2 failed-request Banner flash Banner--error flash-error Banner--full flash-full border-bottom-0">
      <div class="Banner-visual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-stop">
    <path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg>
      </div>
    <div data-view-component="true" class="Banner-message">
      <p class="Banner-title" data-target="x-banner.titleText">Something went really wrong, and we can’t process that file.</p>
        <p>Try again.</p>
</div></div></x-banner>
        </div>
    </div>

    <div class="pr-2 pl-2 pb-2">
      <div data-view-component="true" class="border-right color-border-muted d-inline-block mr-1 pr-2">
        <a href="https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax" target="_blank" rel="noopener noreferrer" data-ga-click="Markdown Toolbar, click, help" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;MARKDOWN_BUTTON&quot;,&quot;label&quot;:null}" data-view-component="true" class="Button--invisible Button--small Button">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-markdown">
    <path d="M14.85 3c.63 0 1.15.52 1.14 1.15v7.7c0 .63-.51 1.15-1.15 1.15H1.15C.52 13 0 12.48 0 11.84V4.15C0 3.52.52 3 1.15 3ZM9 11V5H7L5.5 7 4 5H2v6h2V8l1.5 1.92L7 8v3Zm2.99.5L14.5 8H13V5h-2v3H9.5Z"></path>
</svg>
      </span>
    <span class="Button-label">Markdown is supported</span>
  </span>
</a>
</div>        <button data-file-attachment-for="fc-new_commit_comment_field" data-analytics-event="{&quot;category&quot;:&quot;comment_box&quot;,&quot;action&quot;:&quot;UPLOAD_BUTTON&quot;,&quot;label&quot;:null}" type="button" data-view-component="true" class="Button--invisible Button--small Button">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-image">
    <path d="M16 13.25A1.75 1.75 0 0 1 14.25 15H1.75A1.75 1.75 0 0 1 0 13.25V2.75C0 1.784.784 1 1.75 1h12.5c.966 0 1.75.784 1.75 1.75ZM1.75 2.5a.25.25 0 0 0-.25.25v10.5c0 .138.112.25.25.25h.94l.03-.03 6.077-6.078a1.75 1.75 0 0 1 2.412-.06L14.5 10.31V2.75a.25.25 0 0 0-.25-.25Zm12.5 11a.25.25 0 0 0 .25-.25v-.917l-4.298-3.889a.25.25 0 0 0-.344.009L4.81 13.5ZM7 6a2 2 0 1 1-3.999.001A2 2 0 0 1 7 6ZM5.5 6a.5.5 0 1 0-1 0 .5.5 0 0 0 1 0Z"></path>
</svg>
      </span>
    <span class="Button-label">Paste, drop, or click to add files</span>
  </span>
</button>
    </div>
</file-attachment>
  <div role="tabpanel" class="js-preview-panel overflow-auto CommentBox-comment" aria-labelledby="preview_tab_previewable-comment-form-component-21d5c885-1a44-447f-be27-dd80e88c4d59" hidden="">
    <input type="hidden" name="path" value="" class="js-path">
    <input type="hidden" name="line" value="" class="js-line-number">
    <input type="hidden" name="start_line" value="" class="js-start-line-number">
    <input type="hidden" name="preview_side" value="" class="js-side">
    <input type="hidden" name="preview_start_side" value="" class="js-start-side">
    <input type="hidden" name="start_commit_oid" value="" class="js-start-commit-oid">
    <input type="hidden" name="end_commit_oid" value="" class="js-end-commit-oid">
    <input type="hidden" name="base_commit_oid" value="" class="js-base-commit-oid">
    <input type="hidden" name="comment_id" value="" class="js-comment-id">
    <div class="comment js-suggested-changes-container" data-thread-side="">
  <div class="comment-body markdown-body js-preview-body">
    <p>Nothing to preview</p>
  </div>
</div>

  </div>

  <div class="comment-form-error mb-2 js-comment-update-error" hidden=""></div>
</tab-container>


            <div class="d-flex flex-items-center flex-justify-end gap-2 my-2">
              <button data-disable-invalid="" data-disable-with="" type="submit" data-view-component="true" class="Button--primary Button--medium Button" disabled="">  <span class="Button-content">
    <span class="Button-label">Comment on this commit</span>
  </span>
</button>

            </div>
      </div>
</form>
  </div>

</div>

                <div class="thread-subscription-status js-socket-channel js-updatable-content" data-replace-remote-form-target="" data-channel="eyJjIjoibGlzdC1zdWJzY3JpcHRpb246cmVwb3NpdG9yeTo4NDQ1NjQxOTA6MTE5MTY5NTcwIiwidCI6MTcyNTEzNTUzMX0=--ea3bead41b80ec6f9b73b078c545d0cc93c9340545bbed45171b05cd4bc2591e eyJjIjoidGhyZWFkLXN1YnNjcmlwdGlvbjpjNjUzYjY3NzlmM2I5ZDhmMGU4MjQyOGQ0NWI2NjVjZWVlNTRhNjhjOjExOTE2OTU3MCIsInQiOjE3MjUxMzU1MzF9--ccb390b63c703c8ffb49fee9659f749dcc22ced2c4e57ff11464d150362c7b9e" data-url="/notifications/thread_subscription?repository_id=844564190&amp;thread_class=Commit&amp;thread_id=c653b6779f3b9d8f0e82428d45b665ceee54a68c">
      <!-- '"` --><!-- </textarea></xmp> --><form data-replace-remote-form="true" class="thread-subscribe-form" data-turbo="false" action="https://github.com/notifications/thread" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="0Xo2WioN25gWE1ZJxI31PfRD-3cGYv36NkhtIo0nqZD2Z3T0zexY6UsxFg8uXcPdg2zdEr3WUuuJIa9jA2m-iw" autocomplete="off">        <input type="hidden" name="repository_id" value="844564190">
        <input type="hidden" name="thread_id" value="c653b6779f3b9d8f0e82428d45b665ceee54a68c">
        <input type="hidden" name="thread_class" value="Commit">
        <input type="hidden" name="id" value="subscribe">
        <button data-thread-subscribe-button="" data-disable-with="" aria-describedby="notification-subscribe-button-reason" type="submit" data-view-component="true" class="Button--secondary Button--small Button Button--fullWidth">  <span class="Button-content">
      <span class="Button-visual Button-leadingVisual">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-bell">
    <path d="M8 16a2 2 0 0 0 1.985-1.75c.017-.137-.097-.25-.235-.25h-3.5c-.138 0-.252.113-.235.25A2 2 0 0 0 8 16ZM3 5a5 5 0 0 1 10 0v2.947c0 .05.015.098.042.139l1.703 2.555A1.519 1.519 0 0 1 13.482 13H2.518a1.516 1.516 0 0 1-1.263-2.36l1.703-2.554A.255.255 0 0 0 3 7.947Zm5-3.5A3.5 3.5 0 0 0 4.5 5v2.947c0 .346-.102.683-.294.97l-1.703 2.556a.017.017 0 0 0-.003.01l.001.006c0 .002.002.004.004.006l.006.004.007.001h10.964l.007-.001.006-.004.004-.006.001-.007a.017.017 0 0 0-.003-.01l-1.703-2.554a1.745 1.745 0 0 1-.294-.97V5A3.5 3.5 0 0 0 8 1.5Z"></path>
</svg>
      </span>
    <span class="Button-label">Subscribe</span>
  </span>
</button>
</form>      <p id="notification-subscribe-button-reason" class="reason text-small color-fg-muted" aria-live="polite">
        You’re not receiving notifications from this thread.
      </p>
  </div>

</div>
</div>  </diff-layout>


</div>


  </div>

</turbo-frame>


    </main>
  </div>

  </div>

          <footer class="footer pt-8 pb-6 f6 color-fg-muted p-responsive" role="contentinfo">
  <h2 class="sr-only">Footer</h2>

  


  <div class="d-flex flex-justify-center flex-items-center flex-column-reverse flex-lg-row flex-wrap flex-lg-nowrap">
    <div class="d-flex flex-items-center flex-shrink-0 mx-2">
      <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-2" href="https://github.com/">
        <svg aria-hidden="true" height="24" viewBox="0 0 24 24" version="1.1" width="24" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M12.5.75C6.146.75 1 5.896 1 12.25c0 5.089 3.292 9.387 7.863 10.91.575.101.79-.244.79-.546 0-.273-.014-1.178-.014-2.142-2.889.532-3.636-.704-3.866-1.35-.13-.331-.69-1.352-1.18-1.625-.402-.216-.977-.748-.014-.762.906-.014 1.553.834 1.769 1.179 1.035 1.74 2.688 1.25 3.349.948.1-.747.402-1.25.733-1.538-2.559-.287-5.232-1.279-5.232-5.678 0-1.25.445-2.285 1.178-3.09-.115-.288-.517-1.467.115-3.048 0 0 .963-.302 3.163 1.179.92-.259 1.897-.388 2.875-.388.977 0 1.955.13 2.875.388 2.2-1.495 3.162-1.179 3.162-1.179.633 1.581.23 2.76.115 3.048.733.805 1.179 1.825 1.179 3.09 0 4.413-2.688 5.39-5.247 5.678.417.36.776 1.05.776 2.128 0 1.538-.014 2.774-.014 3.162 0 .302.216.662.79.547C20.709 21.637 24 17.324 24 12.25 24 5.896 18.854.75 12.5.75Z"></path>
</svg>
</a>
      <span>
        © 2024 GitHub,&nbsp;Inc.
      </span>
    </div>

    <nav aria-label="Footer">
      <h3 class="sr-only" id="sr-footer-heading">Footer navigation</h3>

      <ul class="list-style-none d-flex flex-justify-center flex-wrap mb-2 mb-lg-0" aria-labelledby="sr-footer-heading">

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to Terms&quot;,&quot;label&quot;:&quot;text:terms&quot;}" href="https://docs.github.com/site-policy/github-terms/github-terms-of-service" data-view-component="true" class="Link--secondary Link">Terms</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to privacy&quot;,&quot;label&quot;:&quot;text:privacy&quot;}" href="https://docs.github.com/site-policy/privacy-policies/github-privacy-statement" data-view-component="true" class="Link--secondary Link">Privacy</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to security&quot;,&quot;label&quot;:&quot;text:security&quot;}" href="https://github.com/security" data-view-component="true" class="Link--secondary Link">Security</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to status&quot;,&quot;label&quot;:&quot;text:status&quot;}" href="https://www.githubstatus.com/" data-view-component="true" class="Link--secondary Link">Status</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to docs&quot;,&quot;label&quot;:&quot;text:docs&quot;}" href="https://docs.github.com/" data-view-component="true" class="Link--secondary Link">Docs</a>
          </li>

          <li class="mx-2">
            <a data-analytics-event="{&quot;category&quot;:&quot;Footer&quot;,&quot;action&quot;:&quot;go to contact&quot;,&quot;label&quot;:&quot;text:contact&quot;}" href="https://support.github.com/?tags=dotcom-footer" data-view-component="true" class="Link--secondary Link">Contact</a>
          </li>

          <li class="mr-3">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;cookies&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;cookies_link_subfooter_footer&quot;}">
      Manage cookies
    </button>
  </cookie-consent-link>
</li>

<li class="mr-3">
  <cookie-consent-link data-catalyst="">
    <button type="button" class="Link--secondary underline-on-hover border-0 p-0 color-bg-transparent" data-action="click:cookie-consent-link#showConsentManagement" data-analytics-event="{&quot;location&quot;:&quot;footer&quot;,&quot;action&quot;:&quot;dont_share_info&quot;,&quot;context&quot;:&quot;subfooter&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;label&quot;:&quot;dont_share_info_link_subfooter_footer&quot;}">
      Do not share my personal information
    </button>
  </cookie-consent-link>
</li>

      </ul>
    </nav>
  </div>
</footer>




    <ghcc-consent id="ghcc" class="position-fixed bottom-0 left-0" style="z-index: 999999" data-initial-cookie-consent-allowed="" data-cookie-consent-required="false" data-catalyst=""></ghcc-consent>


  <div id="ajax-error-message" class="ajax-error-message flash flash-error" hidden="">
    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-alert">
    <path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"></path>
</svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
    <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
</svg>
    </button>
    You can’t perform that action at this time.
  </div>

    <template id="site-details-dialog"></template>

    <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box color-shadow-large" style="width:360px;"></div>
</div>

    <template id="snippet-clipboard-copy-button"></template>
<template id="snippet-clipboard-copy-button-unpositioned"></template>


    <style>
      .user-mention[href$="/c193249Tasnia"] {
        color: var(--color-user-mention-fg);
        background-color: var(--bgColor-attention-muted, var(--color-attention-subtle));
        border-radius: 2px;
        margin-left: -2px;
        margin-right: -2px;
        padding: 0 2px;
      }
    </style>


    </div>

    <div id="js-global-screen-reader-notice" class="sr-only mt-n1" aria-live="polite" aria-atomic="true">Add files via upload · NTNirjana/session-2--fastapi@c653b67</div>
    <div id="js-global-screen-reader-notice-assertive" class="sr-only mt-n1" aria-live="assertive" aria-atomic="true"></div>
  


</body></html>