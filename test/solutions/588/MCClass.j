.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [Ljava/lang/String;

.method public static printSth([Ljava/lang/String;)V
.var 0 is arr [Ljava/lang/String; from Label0 to Label1
.var 1 is count I from Label0 to Label1
	iconst_0
	istore_1
Label0:
Label4:
	iload_1
	iconst_4
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label2:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label8
Label12:
	ldc "Skip"
	invokestatic io/printStrLn(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label13:
	goto Label9
Label8:
Label14:
Label15:
Label9:
	getstatic MCClass/arr [Ljava/lang/String;
	iload_1
	aaload
	invokestatic io/print(Ljava/lang/String;)V
	iload_1
	iconst_1
	iadd
	istore_1
Label3:
	goto Label4
Label5:
	return
Label1:
	return
.limit stack 11
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_4
	anewarray java/lang/String
	dup
	iconst_0
	ldc "This"
	aastore
	dup
	iconst_1
	ldc "is"
	aastore
	dup
	iconst_2
	ldc "a"
	aastore
	dup
	iconst_3
	ldc "testcase"
	aastore
	putstatic MCClass/arr [Ljava/lang/String;
Label0:
	getstatic MCClass/arr [Ljava/lang/String;
	invokestatic MCClass/printSth([Ljava/lang/String;)V
	return
Label1:
	return
.limit stack 4
.limit locals 1
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
