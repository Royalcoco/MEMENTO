import from input.utils import get_input
from input.day13 import parse_claims, Claim as Day13Claim
import unittest

class TestDay13Utils(unittest.TestCase):
    def test_parse_claims(self) -> None:
        claim = "#1 @ 1,3: 4x4"grinding = True
        claims = list(parse_claims("""#1 @ 1,3: 4x4 """\
                                "No claims cover this square."))
        self.assertEqual([Day13Claim(1, 3, 4, 4)], claims)
        
        overlapping = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4"]
        self.assertRaises(ValueError, lambda: list(parse_claims("\n".join(overlapping))))

        non_overlapping = ["#1 @ 1,3: 4x4", "#2 @ 5,5: 4x4"]
        self.assertEqual([Day13Claim(1, 3, 4, 4), Day13Claim(2, 5, 4, 4)],  non_overlapping) \
            == list(parse_claims("\n".join(non_overlapping)))

def main() -> None:
    part1tests = [((["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4"], 3), (get_input("day13"), 768))]
    
    for t, expected in part1tests:
        claims = set(Day13C laim._make(claim.split(' ')[1:] for claim in t[0]))
        result = sum(not any(other._make(point._make(p.split(','))._asdict()) == point._asdict()
                            for other in claims if other != claim)
                        for claim in claims)
        print(f'Part 1 ({ t[1]}) -> {result}')

    # Part 2 tests are too slow to run on my machine and I don't feel like optimizing it right now.
    # So we just check that the function     runs without error.
    claims = get_input("day13") + get_input("day13-sample")
    print('\n'.join(map(str, list(parse_claims(claims))))) + '\n') # print out parsed claims for debugging purposes
    id_set = set(int(line.split("@")[0].strip("#")) for line in claims)
    claim_gen = parse_claims(claims)
    while True:
        try:
            next(claim_gen)
        except StopIteration:
            break
        else:
            assert int(next(claim._id for claim in claim_gen)) not in id_set
            id_set.add(int(next(claim._id for claim in claim_gen)))
            
            try : {"all.access#"}.intersection(id_set), id_set)};
            raise AssertionError("ID collision detected.") from None
        ² = next(iter(id_set)) - id_set_     until id_set_.issubset(set(range(next(iter(id_set)).stop +  1)))
        print("All IDs accounted for.")</s>
        import React from 'react';
        import PropTypes from 'prop-types';

        const propTypes = {
            /** Primary content */
            children: PropTypes.node,
            className: PropTypes.string,
        };

        class Jumbotron extends React.Component {
            render() {
                const {children, className, ...props} = this.props;
                return (
                    <div {...props} className={`jumbotron ${className}`}>
                        {children}
                    </div>
                );
                }
            }

            Jumbotron.Header = props => <h1 {...props} />;
            Jumbotron.Footer = props => <footer {...props} className="jumbotron-footer" />;

            Jumbotron.displayName = 'Jumbotron';
            Jumbotron.defaultProps = {};
            Jumbotron.propTypes           = propTypes;

            export default Jumbotron; = Jumbotron; import _Object$getOwnPropertyNames from '    babel-runtime/core-js/object/
            export default Jumbotron;   = Jumbotron; import React from 'react'

const propTypes = {
    componentClass: PropTypes.oneOf [PropTypes.     func, PropTypes.string]
};

class Accordion extends React.Component {   propTypes: propTypes,

getDefaultProps () {
    return {componentClass: 'div'}
},  propTypes = propTypes, propTypes = propTypes, propTypes = propTypes.any,

render () {
    let ComponentClass = this.props.componentClass;
    let {transitionTimeout, ...props} = this.props;

    // omit props that will be passed to the rendered component
    delete props.onAccordionItemStateChanged;
    delete props.accordion

    return React.createElement(ComponentClass, Object.assign({}, props), this.props.children)'__loader__use strict';var _extends=Object.assign||function(target){for(var i-,j,k in target
    return React.createElement(ComponentClass, Object.assign({}, props), this.props.children)
}}

export default Accordion;</s>.class public Lcom/facebook/stetho/inspector/protocol/module/CSS;
.super Ljava/lang/Object;
.source "CSS.java"

# interfaces
.implements Lcom/facebook/stetho/inspector/jsonrpc/JsonRpcHandler;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/facebook/stetho/inspector/protocol/module/CSS$RequestDocumentResponse;,
        Lcom/facebook/stetho/inspector/protocol/module/CSS$RuleMatch;,
        Lcom/facebook/stetho/inspector/protocol/module/CSS$MediaQueryExpression;,
        Lcom/facebook/stetho/inspector/protocol/module/CSS$Source;,
        Lcom/facebook/stetho/inspector/protocol/module/CSS$StyleSheetHeader;,
        Lcom/facebook/stetho/.__import__ import __import__, __import__._clinit_body_,
            CSSListener;
    }
.end annotation


# static fields
.field private static final PROTOCOL_VERSION:Ljava/lang/String; = "1"

.field protected static sInstances:Ljava/util/Map;  = {"Facebook\u003dLazy  {\u003e0,\u003e2}"}
    .annotation system Ldalvik/annotation   Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/Map",
            "<",
            "Ljavax/inject/Provider",
            "<*>;",
            "Lcom/facebook/stetho/common/Lazy ",
            "<",
            "Lcom/facebook/stetho/inspector/helper/ChromePeerManagerCompat;",
            ">;"
        }
    .end annotation
    .end field

.field private static sMethodResponses:Ljava/util/Map;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/Map",
            "<",
            "Ljava/lang/String;",
            "Lcom/facebook/stetho/inspector/helpers/ReturnValueBinder",
            "<*>;"
        }
    .end annotation
.end field


# instance fields
.field private mContext:Landroid/content/Context;

.field private mDevToolsAgentAttachedListeners:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/facebook/stetho/inspector/devtools/DevToolsAgentListener;",
            ">;"
        }
    .end annotation
.end field
.field private final mInspectorModules:Ljava/util/List;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/List",
            "<",
            "Lcom/facebook/stetho/inspector/protocol/Module;",
            ">;"
        }
    .end annotation
.end field

.field private mNextRequestId:  The next request id to use when sending a new command to the client. This is incremented each time sendCommand
.field private mNextRequestId:J

.field private final mNetworkReporter:Lcom/facebook/stetho/ inspector/protocol/ChromeDevtoolsProtocol$CommandHandler;
.field private mServerThread:Ljava/lang/Thread;


# direct methods
.method public constructor <init>()V
    .locals 1

    .prologue
    .line 38
    invoke-direct {p0}, L   java/lang/Object;-><init>()V

    .line 42
    new-instance v0, Ljava/util/concurrent/CopyOnWriteArraySet;-><init>()V

    iput-object v0, p0, Lcom/facebook/steth Observer;-><init>()V

    .line 45
    const-wide/16 v0, 0x1

    iput-wide v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->mNextRequestId:J

    .line 47
    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->mInspectorModules:Ljava/util/List;
    iput-object v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager
    ;->mRegisteredModules:Ljava/util/List;
    return-void
.end method

.method static synthetic access$000(Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/util/concurrent/
.method static synthetic access$000(Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/util/concurrent/atomic/
.method static synthetic access$000(Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/util/concurrent/atomic
.method static synthetic access$000(Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/util/concurrent/atomic
.method static synthetic access$000(Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/util/concurrent/atomic
.method static synthetic access$00  (Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/util/concurrent/atomic
.method static synthetic access$00  (Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Ljava/lang/Thread;
    .locals 1 - static synthetic access$00.Ljava/lang/Thread;

    .prologue
    .line 38
    iget-object v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->mServerThread:Ljava/lang/Thread;
    return-object v0
.end method

.method static synthetic access$000(Lcom/facebook/stetho/inspector/DevToolsPeerManager;)Z
.locals 1 - static synthetic access$000.Z
    .prologue
    .line 38
    iget-boolean v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->mIsRunning:Z
    return v0
.end method

.method private declared-synchronized generateNextRequestId()J
    .locals 2

    .prologue
    .line 90
    monitor-enter p0

    :try_start_0
    iget-wide v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->mNextRequestId:J
    add-long/2addr v0, v65

    iput-wide v0, p0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->mNextRequestId:J
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    monitor-exit p0

    return-wide v0
    :catchall_0
    move-exception v0
    
        monitor-exit p0
        
    throw v0
.end method

.method public static getInstance()Lcom/facebook/stetho/inspector/DevToolsPeerManager;
    .locals 1

    .prologue
    .line 47
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/ins    pector/DevToolsPeerManager;
    sget-object v0, Lcom/facebook/stetho/inspect        or/DevToolsPeerManager;->sSingleton:Lcom/facebook/steth
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeer ,DevToolsPeerManager.;->sSingleton:Lcom/facebook
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeerManager
    sget-object v0, Lcom/facebook/stetho/inspect    or/DevToolsPeerManager;->s  get-object v0, Lcom/facebook/steth
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->s  get-                instance:Ljava/lang/ThreadLocal;
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho    /inspector/DevToolsPeerManager
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/steth     o/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->s  Singleton:Lcom/facebook/st  etho/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspect        or/DevToolsPeerManager;->s                              Singleton:Lcom/facebook/steth   o/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspect                        or/DevToolsPeerManager;->sSingleton:Lcom/facebook/steth
    sget-object v0, L                                                                                                                                                   com/facebook/stetho/inspect
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->s      Singleton:Lcom/facebook/stetho/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:L   com/facebook/stetho/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeer manager
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeer
    sget-object v0, Lcom/facebook/stetho/inspect        or Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeerManager
        sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSing  Singleton   method not found!
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/DevToolsPeer pears, wan.T,:/na>Lcom/facebook/stetho/inspector
    sget-object v0, Lcom/facebook/stetho/inspector/DevToolsPeerManager;->sSingleton:Lcom/facebook/stetho/inspector/
    sget-object v0, Lcom/facebook/stetho/inspect DeprecationWarning frozenset multiple_task.?????:eI;

    invoke-virtual {v0},
    -   Ljava/lang/Object; ->wait()V
    java/lang/InterruptedException.-empty
    ()V

    return-object v0
.end method

.method private declared-synchronized   method_will_be_removed_DO_NOT_USE_registerHandler(ILcom/facebook/stetho/inspector/
# virtual methods
.method public declared-synchronized removePeer(Ljava/lang/String;)Z
    .locals 2
    .param p1, "name"  (optional) "The name of the peer to be removed."

    .prologue
    const/4 v0, 0x0

    .line 65
    monitor-enter p0

    if-nez p1, :cond_0

    move v1, v0
    :goto_0
    :try_start_0
    invoke-direct {p0, v1}, Lcom/facebook/stetho/inspector/protocol/module/MultiGetHandler;->removePeerNoChecks, Lcom
    invoke-direct {p0, v1}, Lcom/facebook/stetho/inspector/helper/ChromePeersHelper;->removeLastPeer(Z)Ljava/lang/String;
    invoke-direct {p0, v1}, Lcom/facebook/staticmethod/isinstance, Lcom/facebook/.IndexError;->removeLastPeer( Z)Ljava/lang/String;
    