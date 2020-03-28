{ 桁DP }
var
  N: string;
  K: Integer;
  A: Integer;
  B: array[0..3] of Integer;
  T: Integer;
  I: Integer;
  J: Integer;
begin
  readln(N);
  read(K);

  A := 1;
  B[0] := 1;
  B[1] := Ord(N[1]) - 48 - 1;

  for I := 2 to Length(N) do
  begin
    T := Ord(N[I]) - 48;
    for J :=  K - 1 downto 0 do
    begin
      B[j + 1] := B[j + 1] + b[j] * 9;
    end;
    if T <> 0 then
    begin
      if A + 1 <= K then B[A + 1] := B[A + 1] + T - 1;
      if A <= K then Inc(B[A]);
      Inc(A);
    end;
  end;

  if A = K then writeln(B[K] + 1)
  else writeln(B[K]);
end.
