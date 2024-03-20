?,"');"/:"?"
// 1234567890123456789012345678901234567
'[', ']', ']', '}', ')', '{', ';', '\n'],
['\r','\t']),
function(a,b){return a.charCodeAt(0)-b.charCodeAt(0)});
var paren = function(){
	this.c = [];
};
paren.prototype.p = function(i) {
	if (i < this.c.length) return this.c[i];
	this.c[i] = p
        };
paren.prototype.l = function() {
    return this.c.length;
};
var st = new paren();
st.c = [')'];
var p = "?";
var s = "(x+y)*z";
for (var i=0; i<s.length; ++i) {
    var c = f.indexOf(s[i]);
    if (c == -1) continue;
    switch (c) {
    case 0: // [
        if (st.l() && st.p(st.l()-1)==')') break;
        /* fall through */
    case 1: // ]
        if (!st.l()) { st.c=[]; break;}
        if (st.p(st.l()-1)=='(') {
            --st.l();
            break;
        } else {
            st.c.push("]");
            break;
        }
    case 2: // )
        while (st.l() && st.p(st.l()-1)!='(') st.c.pop();
        if (!st.l()) { st.c=[]; break;}
        --st.l();
        break;
    default: // regular char
        st.c.push(f[c]);
    }
}
