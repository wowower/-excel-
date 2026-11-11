(function(root){
'use strict';
const DAY=86400000;
function validDate(s){if(typeof s!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(s))return false;const d=new Date(s+'T00:00:00Z');return Number.isFinite(+d)&&d.toISOString().slice(0,10)===s;}
function validate(r){
 if(!r||typeof r!=='object'||!validDate(r.date)||!/^([01]\d|2[0-3]):[0-5]\d$/.test(r.time))throw Error('日期或时间无效');
 if(typeof r.id!=='string'||!r.id||r.id.length>100)throw Error('记录编号无效');
 if(!['morning','evening','other'].includes(r.period))throw Error('测量时段无效');
 if(!Number.isInteger(r.sys)||!Number.isInteger(r.dia)||r.sys<40||r.sys>300||r.dia<20||r.dia>200||r.sys<=r.dia)throw Error('请核对读数：收缩压 40–300、舒张压 20–200，且收缩压应更高。这是输入范围，不是健康范围。');
 if(r.pulse!==null&&(!Number.isInteger(r.pulse)||r.pulse<20||r.pulse>250))throw Error('脉搏请填 20–250 的整数，或留空');
 if(typeof r.note!=='string'||r.note.length>300)throw Error('备注最多 300 字');
 return {id:r.id,date:r.date,time:r.time,period:r.period,sys:r.sys,dia:r.dia,pulse:r.pulse,note:r.note};
}
function urgent(sys,dia,symptoms){
 if(symptoms)return {level:'emergency',text:'如现在出现胸痛、呼吸困难、突发无力、言语或视力异常等症状，请立即拨打当地急救电话（中国大陆 120）。不要等待记录、计时或血压自行下降。'};
 if(Number(sys)>=180||Number(dia)>=120)return {level:'urgent',text:'读数达到或超过 180/120 阈值之一：无上述症状时，静坐至少 1 分钟后复测；仍然很高，请立即联系医疗人员。出现症状立即呼叫急救。'};
 return {level:'neutral',text:'记录用于就诊沟通，不能排除急症或作出诊断。不要自行停药或调整剂量；不适或对读数有疑问时联系医疗人员。'};
}
function windowRows(rows,start,excludeFirst){if(!validDate(start))throw Error('请选择有效的起始日期');const first=Date.parse(start+'T00:00:00Z');return rows.filter(r=>{const t=Date.parse(r.date+'T00:00:00Z');return t>=first+(excludeFirst?DAY:0)&&t<first+7*DAY;}).sort((a,b)=>(a.date+'T'+a.time).localeCompare(b.date+'T'+b.time));}
function summary(rows){const n=rows.length;return {n,days:new Set(rows.map(r=>r.date)).size,sys:n?rows.reduce((s,r)=>s+r.sys,0)/n:null,dia:n?rows.reduce((s,r)=>s+r.dia,0)/n:null};}
function importData(text){let x;try{x=JSON.parse(text);}catch{throw Error('不是有效的 JSON 备份');}if(x?.format!=='home-bp-journal'||x.version!==1||!Array.isArray(x.records)||x.records.length>10000)throw Error('备份格式不支持，或记录超过 10,000 条');const rows=x.records.map(validate);if(new Set(rows.map(r=>r.id)).size!==rows.length)throw Error('备份中有重复记录编号');return rows;}
root.BP={validDate,validate,urgent,windowRows,summary,importData};if(typeof module!=='undefined')module.exports=root.BP;
})(globalThis);
