program abc129e;
const
  M = 1000000007;
var
  L: string;
  I, T, Result: Int64;
begin
  Read(L);

  Result := 1;
  T := 1;
  for I := Length(L) downto 1 do
  begin
    if L[i] = '1' then
    begin
      Result := Result * 2 + t;
      Result := Result mod M;
    end;
    T := T * 3;
    T := T mod M;
  end;
  WriteLn(Result);
end.
