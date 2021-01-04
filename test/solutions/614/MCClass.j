.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is n I from Label0 to Label1
	bipush 120
	istore_1
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	sipush 867
	iastore
	dup
	iconst_1
	sipush 345
	iastore
	dup
	iconst_2
	sipush 987
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 76
	iastore
	dup
	iconst_1
	bipush 12
	iastore
	dup
	iconst_2
	sipush 744
	iastore
	aastore
	astore_2
Label0:
	iload_1
	bipush 10
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
Label6:
	iload_1
	bipush 11
	irem
	bipush 10
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iload_1
	aload_2
	iconst_1
	aaload
	iconst_0
	iaload
	if_icmple Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label12
	iconst_0
	goto Label13
Label12:
	iconst_1
Label13:
	ifle Label8
Label16:
	aload_2
	iconst_0
	aaload
	iconst_1
	iaload
	iload_1
	imul
	bipush 9
	irem
	iconst_3
	idiv
	istore_1
Label17:
	goto Label9
Label8:
Label18:
Label19:
Label9:
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label7:
	goto Label3
Label2:
Label20:
Label21:
Label3:
Label1:
	return
.limit stack 25
.limit locals 3
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
