.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 7
	istore_1
Label0:
	iload_1
	iconst_4
	irem
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label2
Label8:
	iconst_0
	istore_1
Label9:
	goto Label5
Label2:
	iload_1
	iconst_4
	irem
	iconst_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label3
Label12:
	iconst_1
	istore_1
Label13:
	goto Label5
Label3:
	iload_1
	iconst_4
	irem
	iconst_2
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label4
Label16:
	iconst_2
	istore_1
Label17:
	goto Label5
Label4:
Label18:
	iconst_3
	istore_1
Label19:
Label5:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
	return
.limit stack 18
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
