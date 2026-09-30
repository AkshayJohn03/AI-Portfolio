import json

wavs = {"01":21.973,"02":22.379,"03":22.507,"04":40.954,"05":31.141,"06":34.405,
        "07":26.944,"08":33.551,"09":26.795,"10":35.215,"11":25.92,"12":23.787,
        "13":33.893,"14":11.051}
starts = {"01":0.0,"02":22.67,"03":45.75,"04":68.96,"05":110.61,"06":142.45,
          "07":177.56,"08":205.2,"09":239.45,"10":266.95,"11":302.87,"12":329.49,
          "13":353.98,"14":388.57}

S = {}
D = "D:/aria/Projects/brag-output/composition/assets/voiceover/script"
for k in wavs:
    S[k] = open(f"{D}/s{k}.txt", encoding="utf-8").read()

def widx(k, needle):
    pos = S[k].lower().find(needle.lower())
    if pos < 0: raise SystemExit(f"NOT FOUND s{k}: {needle}")
    return len(S[k][:pos].split())

def t(k, needle):
    return round(starts[k] + widx(k, needle) / len(S[k].split()) * wavs[k], 2)

out = {}
def add(key, k, needle):
    out[key] = t(k, needle)

# S1
add("s1_strike", "01", "weekend")
add("s1_job", "01", "different job")
add("s1_c1", "01", "breaks silently")
add("s1_c2", "01", "bills")
add("s1_c3", "01", "attackers")
add("s1_c4", "01", "when it fails")
add("s1_banner", "01", "this portfolio")
# S2
add("s2_llm", "02", "autocomplete")
add("s2_pipe", "02", "around it sits")
add("s2_boxes", "02", "fetch documents")
add("s2_assembly", "02", "every serious")
# S3
add("s3_st1", "03", "head waiter")
add("s3_st2", "03", "food critic")
add("s3_st3", "03", "c c t v")
add("s3_st4", "03", "brigade")
add("s3_st5", "03", "sous-chef")
add("s3_st6", "03", "mystery diner")
add("s3_st7", "03", "real customer")
add("s3_st8", "03", "gets served")
add("s3_bell", "03", "let's walk")
# S4
add("s4_st", "04", "station one")
add("s4_gateway", "04", "talks to the gateway")
add("s4_breaker", "04", "circuit breaker")
add("s4_fallback", "04", "fallback")
add("s4_cache", "04", "semantic cache")
add("s4_autopilot", "04", "cost autopilot")
add("s4_ledger", "04", "usage ledger")
add("s4_readout", "04", "measured load")
add("s4_p95", "04", "p ninety five")
# S5
add("s5_st", "05", "station two")
add("s5_rubric", "05", "rubric")
add("s5_kappa", "05", "kappa")
add("s5_regression", "05", "regression")
add("s5_gate", "05", "c i gate")
add("s5_stamp", "05", "blocks the release")
# S6
add("s6_st", "06", "station three")
add("s6_trace", "06", "leaves a trace")
add("s6_taxonomy", "06", "taxonomy")
add("s6_circle", "06", "guilty stage")
add("s6_pr", "06", "precision and recall")
add("s6_readout", "06", "planted failures")
# S7
add("s7_st", "07", "station four")
add("s7_agent", "07", "research team")
add("s7_dag", "07", "task graph")
add("s7_receipts", "07", "receipts")
add("s7_resume", "07", "resumes")
add("s7_hall", "07", "hallucination rate")
add("s7_readout", "07", "offline corpus")
# S8
add("s8_st", "08", "station five")
add("s8_funnel", "08", "worked examples")
add("s8_rejection", "08", "rejection sampling")
add("s8_decon", "08", "decontamination")
add("s8_qlora", "08", "compressed base model")
add("s8_readout", "08", "measured run")
# S9
add("s9_st", "09", "station six")
add("s9_resume_card", "09", "job application")
add("s9_injection", "09", "prompt injection")
add("s9_asr", "09", "attack success rate")
add("s9_count", "09", "ninety two percent")
add("s9_zero", "09", "hardened: zero")
# S10
add("s10_st", "10", "station seven")
add("s10_rag", "10", "the copilot chunks")
add("s10_hybrid", "10", "keyword and by meaning")
add("s10_fast", "10", "fast path")
add("s10_refuse", "10", "refuses and escalates")
add("s10_recall", "10", "recall at five")
add("s10_readout", "10", "safety violations")
# S11
add("s11_st", "11", "station eight")
add("s11_lab", "11", "lab space")
add("s11_idem", "11", "idempotent")
add("s11_receipt", "11", "receipt")
add("s11_readout", "11", "sixty five audited")
# S12
add("s12_offline", "12", "runs offline")
add("s12_mock", "12", "mock clients")
add("s12_recall", "12", "recall:")
add("s12_precision", "12", "precision:")
add("s12_asr", "12", "a s r")
add("s12_p95", "12", "p ninety five")
# S13
add("s13_flow", "13", "one request flows")
add("s13_gateway", "13", "metered and cached")
add("s13_fq", "13", "spans go to forensiq")
add("s13_gate", "13", "gate passes")
add("s13_exit0", "13", "exit zero")
add("s13_exit1", "13", "exit one")
add("s13_list", "13", "to learn it in order")
add("s13_readout", "13", "forty four spans")
# S14
add("s14_title", "14", "that's the map")

print(json.dumps(out, indent=1))
